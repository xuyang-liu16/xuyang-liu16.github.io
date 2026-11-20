# Reference: https://github.com/song-chen1/song-chen1.github.io
import json
import os
import time
from datetime import datetime, timezone
from urllib.parse import parse_qs, urljoin, urlparse

from bs4 import BeautifulSoup
from curl_cffi import requests
from curl_cffi.requests.exceptions import RequestException


SCHOLAR_URL = "https://scholar.google.com/citations"
SCHOLAR_ENDPOINTS = (
    SCHOLAR_URL,
    "https://scholar.google.com.hk/citations",
    "https://scholar.google.com.sg/citations",
)
PAGE_SIZE = 100
CANONICAL_PUBLICATION_IDS = {
    "Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models":
        "9VhMC1QAAAAJ:CHSYGLWDkRkC",
    "Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models":
        "9VhMC1QAAAAJ:1sJd4Hv_s6UC",
}


def fetch_page(session, scholar_id, start, max_attempts=3):
    last_error = None
    for attempt in range(1, max_attempts + 1):
        endpoint = SCHOLAR_ENDPOINTS[(attempt - 1) % len(SCHOLAR_ENDPOINTS)]
        try:
            response = session.get(
                endpoint,
                params={
                    "user": scholar_id,
                    "hl": "en",
                    "pagesize": PAGE_SIZE,
                    "cstart": start,
                },
                timeout=(10, 30),
            )
            response.raise_for_status()
            page = BeautifulSoup(response.text, "html.parser")
            if not page.select_one("#gsc_prf_in") or not page.select("#gsc_rsb_st td.gsc_rsb_std"):
                raise ValueError("Google Scholar did not return a public author profile")
            return page
        except (RequestException, ValueError) as exc:
            last_error = exc
            print(
                f"Scholar page {start}, attempt {attempt}/{max_attempts} "
                f"via {endpoint}: {exc}",
                flush=True,
            )
            if attempt < max_attempts:
                time.sleep(5 * attempt)

    raise RuntimeError(f"Failed to fetch Google Scholar page {start}: {last_error}")


def parse_number(text):
    return int(text.replace(",", "").replace("\u202f", "").strip())


def parse_author(page, scholar_id):
    author = {
        "container_type": "Author",
        "filled": ["basics", "publications", "indices", "counts"],
        "scholar_id": scholar_id,
        "source": "AUTHOR_PROFILE_PAGE",
        "name": page.select_one("#gsc_prf_in").get_text(strip=True),
    }
    rows = page.select("#gsc_rsb_st tbody tr")
    for row, field in zip(rows, ("citedby", "hindex", "i10index")):
        cells = row.select("td.gsc_rsb_std")
        if len(cells) != 2:
            raise ValueError(f"Missing Google Scholar {field} counts")
        author[field] = parse_number(cells[0].get_text())
        author[field + "5y"] = parse_number(cells[1].get_text())
    if "citedby" not in author or len(rows) != 3:
        raise ValueError("Incomplete Google Scholar metrics table")
    author["cites_per_year"] = {
        year.get_text(strip=True): parse_number(count.get_text())
        for year, count in zip(page.select(".gsc_g_t"), page.select(".gsc_g_al"))
    }
    return author


def parse_publications(page, scholar_id):
    publications = {}
    for row in page.select(".gsc_a_tr"):
        title_link = row.select_one("a.gsc_a_at")
        citation_link = row.select_one("a.gsc_a_ac")
        if title_link is None or citation_link is None:
            raise ValueError("Incomplete Google Scholar publication row")
        query = parse_qs(urlparse(title_link.get("href", "")).query)
        publication_id = query.get("citation_for_view", [""])[0]
        if not publication_id.startswith(scholar_id + ":"):
            raise ValueError("Publication does not belong to the requested Scholar profile")
        title = title_link.get_text(strip=True)
        publication_id = CANONICAL_PUBLICATION_IDS.get(title, publication_id)
        citation_url = urljoin(SCHOLAR_URL, citation_link.get("href", ""))
        cite_ids = parse_qs(urlparse(citation_url).query).get("cites", [""])[0]
        description = row.select(".gs_gray")
        year = row.select_one(".gsc_a_y")
        publications[publication_id] = {
            "container_type": "Publication",
            "source": "AUTHOR_PUBLICATION_ENTRY",
            "bib": {
                "title": title,
                "pub_year": year.get_text(strip=True) if year else "",
                "citation": description[-1].get_text(" ", strip=True) if description else "",
            },
            "filled": False,
            "author_pub_id": publication_id,
            "num_citations": parse_number(citation_link.get_text() or "0"),
            "citedby_url": citation_url,
            "cites_id": cite_ids.split(",") if cite_ids else [],
        }
    return publications


def fetch_author(scholar_id):
    with requests.Session(impersonate="chrome") as session:
        page = fetch_page(session, scholar_id, 0)
        author = parse_author(page, scholar_id)
        publications = {}
        start = 0
        while True:
            batch = parse_publications(page, scholar_id)
            if not batch or publications.keys() & batch.keys():
                raise ValueError("Google Scholar returned empty or repeated publication results")
            publications.update(batch)
            more = page.select_one("#gsc_bpf_more")
            if more is not None and more.has_attr("disabled"):
                break
            if len(batch) < PAGE_SIZE:
                break
            start += PAGE_SIZE
            page = fetch_page(session, scholar_id, start)
    author["publications"] = publications
    return author


def main():
    scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
    author = fetch_author(scholar_id)
    author["updated"] = datetime.now(timezone.utc).isoformat()

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author.get('citedby', 0)}",
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)
    print(
        f"Updated {author['name']}: {author['citedby']} citations, "
        f"{len(author['publications'])} publications at {author['updated']}",
        flush=True,
    )


if __name__ == "__main__":
    main()
