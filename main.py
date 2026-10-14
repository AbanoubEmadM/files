# main.py
import logging
import os

from serpapi_source import GOOGLE_JOBS_QUERIES, fetch_google_jobs
from config import MAX_ALERTS_PER_RUN, SEARCH_TERMS
from filters import is_relevant
from notifier import send_job_alert
from scrapers import SOURCES, fetch_source
from storage import is_seen, mark_seen

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger("internship-bot")


def run() -> None:
    candidates = {}  # url -> job, so each posting is handled once per run

    for track, queries in SEARCH_TERMS.items():
        for query in queries:
            for source in SOURCES:
                for job in fetch_source(source, query):
                    candidates.setdefault(job["url"], job)
    # Google Jobs runs only when the RUN_GOOGLE_JOBS environment variable is "1".
    # Schedule it once a day to stay within the free quota.
    if os.environ.get("RUN_GOOGLE_JOBS") == "1":
        for query in GOOGLE_JOBS_QUERIES:
            for job in fetch_google_jobs(query):
                candidates.setdefault(job["url"], job)
    log.info("Collected %d unique postings across all sources", len(candidates))
    per_source = {}
    for job in candidates.values():
        per_source[job["source"]] = per_source.get(job["source"], 0) + 1
    log.info("Per source: %s", per_source or "none")

    new_matches = [
        job for job in candidates.values()
        if is_relevant(job["title"], job["description"])
        and not is_seen(job["url"])
    ]
    log.info("%d new relevant postings", len(new_matches))

    sent = 0
    for job in new_matches[:MAX_ALERTS_PER_RUN]:
        if send_job_alert(job):
            mark_seen(job["url"], job["title"], job["source"])
            sent += 1

    skipped = len(new_matches) - sent
    if skipped > 0:
        log.info("Stopped after %d alerts; %d left for the next run", sent, skipped)
    log.info("Done. Sent %d alerts.", sent)


if __name__ == "__main__":
    run()
