# debug_google.py
from serpapi_source import GOOGLE_JOBS_QUERIES, fetch_google_jobs
from filters import is_relevant
from storage import is_seen
from filters import relevance_reason

for query in GOOGLE_JOBS_QUERIES:
    for job in fetch_google_jobs(query):
        print(f"TITLE: {job['title']}")
        print(f"URL:   {job['url']}")
        print(f"relevant={is_relevant(job['title'], job['description'])}  "
              f"already_seen={is_seen(job['url'])}")
        print(f"reason={relevance_reason(job['title'], job['description'])}  "
              f"already_seen={is_seen(job['url'])}")
        print("-" * 40)