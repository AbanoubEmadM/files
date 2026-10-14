# serpapi_source.py
import logging
import os
import time

import requests

log = logging.getLogger(__name__)

API_KEY = os.environ.get("SERPAPI_KEY", "")
ENDPOINT = "https://serpapi.com/search.json"

# Keep this list short: each query uses one search from your monthly quota.
GOOGLE_JOBS_QUERIES = [
    "linux intern Egypt",
    "network engineer intern Cairo",
    "system administrator intern Egypt",
    "IT support intern Cairo",
]


def fetch_google_jobs(query: str) -> list[dict]:
    if not API_KEY:
        log.error("SERPAPI_KEY is not set; skipping Google Jobs")
        return []

    params = {
        "engine": "google_jobs",
        "q": query,
        "hl": "en",
        "api_key": API_KEY,
    }

    data = None
    for attempt in range(1, 4):  # up to 3 attempts
        try:
            resp = requests.get(ENDPOINT, params=params, timeout=60)
            resp.raise_for_status()
            data = resp.json()
            break
        except (requests.RequestException, ValueError) as exc:
            log.warning("google_jobs: attempt %d failed for %r: %s", attempt, query, exc)
            if attempt < 3:
                time.sleep(5 * attempt)

    if data is None:
        return []

    jobs = []
    for item in data.get("jobs_results", []):
        title = item.get("title", "").strip()
        if not title:
            continue

        company = item.get("company_name", "")
        location = item.get("location", "")

        # Try each possible link field, skipping Google's own search pages.
        link = ""
        candidates = [item.get("share_link", "")]
        candidates += [opt.get("link", "") for opt in item.get("apply_options", [])]
        candidates += [rel.get("link", "") for rel in item.get("related_links", [])]
        for candidate in candidates:
            if candidate and "google.com/search" not in candidate:
                link = candidate
                break

        if link:
            url = link.split("?")[0]
        else:
            # No direct link: use a stable key so duplicates still collapse.
            url = f"gjobs://{title}|{company}|{location}".lower()

        jobs.append({
            "source": "google_jobs",
            "title": title,
            "url": url,
            "description": " ".join([
                title,
                company,
                location,
                item.get("description", "")[:1500],
            ]),
        })

    return jobs