from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import sys
import signal


def _setup_timeout(seconds: int) -> None:
    if seconds <= 0:
        return

    def _handle_timeout(signum, frame):
        print(f"Error: script exceeded {seconds}s and was aborted.", file=sys.stderr)
        sys.exit(124)

    # SIGALRM is available on Linux runners (used by GitHub Actions ubuntu-latest)
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, _handle_timeout)
        signal.alarm(seconds)


def _configure_proxy_from_env() -> None:
    # Prefer SerpAPI if key is available; this avoids scraping/CAPTCHA and is reliable.
    serpapi_key = os.environ.get("SERPAPI_API_KEY", "").strip()
    if serpapi_key:
        pg = ProxyGenerator()
        if pg.SerpAPI(api_key=serpapi_key):
            scholarly.use_proxy(pg)
            print("Info: Using SerpAPI backend for scholarly.")
            return
        print("Warning: Failed to initialize SerpAPI backend, falling back to default.", file=sys.stderr)

    # Otherwise, keep default backend. Avoid FreeProxies here to reduce flakiness/timeouts.


def _fetch_author_data(google_scholar_id: str) -> dict:
    author: dict = scholarly.search_author_id(google_scholar_id)
    # Limit sections to reduce scraping volume
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
    author["updated"] = str(datetime.now())
    author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}
    return author


def main() -> int:
    timeout_seconds = int(os.environ.get("SCHOLAR_TIMEOUT_SECONDS", "240"))
    _setup_timeout(timeout_seconds)
    _configure_proxy_from_env()

    google_scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not google_scholar_id:
        print("Error: GOOGLE_SCHOLAR_ID is not set.", file=sys.stderr)
        return 2

    try:
        author = _fetch_author_data(google_scholar_id)
    except Exception as exc:  # noqa: BLE001 keep broad to fail fast in CI
        print(f"Error: failed to fetch scholar data: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(author, indent=2))
    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)

    return 0


if __name__ == "__main__":
    sys.exit(main())
