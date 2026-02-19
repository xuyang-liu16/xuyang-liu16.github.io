# Reference: https://github.com/song-chen1/song-chen1.github.io
import json
import os
import time
from datetime import datetime, timezone

from scholarly import scholarly


def fetch_author_with_retry(scholar_id: str, max_attempts: int = 3):
    last_error = None
    for attempt in range(1, max_attempts + 1):
        try:
            author = scholarly.search_author_id(scholar_id)
            if not author:
                raise RuntimeError(f"Author not found for GOOGLE_SCHOLAR_ID={scholar_id}")

            scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])

            # Refresh each publication to avoid stale per-paper citation counts.
            refreshed_publications = []
            for pub in author.get("publications", []):
                try:
                    refreshed_publications.append(scholarly.fill(pub))
                except Exception:
                    refreshed_publications.append(pub)
            author["publications"] = refreshed_publications
            return author
        except Exception as exc:
            last_error = exc
            if attempt < max_attempts:
                time.sleep(5 * attempt)

    raise RuntimeError(f"Failed to fetch Google Scholar data after {max_attempts} attempts: {last_error}")


def main():
    scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
    author = fetch_author_with_retry(scholar_id)

    author["updated"] = datetime.now(timezone.utc).isoformat()
    author["publications"] = {
        v["author_pub_id"]: v
        for v in author.get("publications", [])
        if isinstance(v, dict) and v.get("author_pub_id")
    }

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


if __name__ == "__main__":
    main()
