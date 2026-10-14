# scrapers.py
import logging
import re
import time
from urllib.parse import quote_plus, urljoin

import requests
from bs4 import BeautifulSoup

from config import REQUEST_DELAY

log = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
}
TIMEOUT = 20

# Each source: where to search, and a regex that matches job-detail links.
# If a source returns 0 results, check the link pattern against the real HTML.
SOURCES = {
    "wuzzuf": {
        "base": "https://wuzzuf.net",
        "search": "https://wuzzuf.net/search/jobs/?q={query}",
        "link_pattern": re.compile(r"/jobs/p/"),
    },
}


def fetch_source(name: str, query: str) -> list[dict]:
    """Search one source for one query and return a list of job dicts."""
    cfg = SOURCES[name]
    url = cfg["search"].format(query=quote_plus(query))

    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException as exc:
        log.warning("%s: request failed for %r: %s", name, query, exc)
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    jobs, seen_urls = [], set()

    for link in soup.find_all("a", href=cfg["link_pattern"]):
        title = link.get_text(strip=True)
        if not title:
            continue

        job_url = urljoin(cfg["base"], link["href"]).split("?")[0]
        if job_url in seen_urls:
            continue
        seen_urls.add(job_url)

        # Use the enclosing card as the description so filters can see
        # location and requirements text near the title.
        card = link.find_parent(["article", "li", "div"]) or link
        description = card.get_text(" ", strip=True)[:1500]

        jobs.append({
            "source": name,
            "title": title,
            "url": job_url,
            "description": description,
        })

    time.sleep(REQUEST_DELAY)
    return jobs
