# Reference: https://github.com/song-chen1/song-chen1.github.io
import json
import os
import signal
import time
from datetime import datetime, timezone

from scholarly import scholarly


class TimeoutError(RuntimeError):
    pass


def _timeout_handler(signum, frame):
    raise TimeoutError("Google Scholar request timed out")


def call_with_timeout(func, seconds, *args, **kwargs):
    previous = signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(seconds)
    try:
        return func(*args, **kwargs)
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)


def fetch_author_with_retry(scholar_id: str, max_attempts: int = 3):
    last_error = None
    for attempt in range(1, max_attempts + 1):
        try:
            author = call_with_timeout(scholarly.search_author_id, 120, scholar_id)
            if not author:
                raise RuntimeError(f"Author not found for GOOGLE_SCHOLAR_ID={scholar_id}")

            # Keep this bounded: a single stuck request should fail fast and retry.
            call_with_timeout(
                scholarly.fill,
                180,
                author,
                sections=["basics", "indices", "counts", "publications"],
            )
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
