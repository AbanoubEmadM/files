# storage.py
import sqlite3
from pathlib import Path

DB_PATH = Path("seen_jobs.db")


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS seen_jobs (
            url        TEXT PRIMARY KEY,
            title      TEXT,
            source     TEXT,
            first_seen TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    return conn


def is_seen(url: str) -> bool:
    with _connect() as conn:
        row = conn.execute("SELECT 1 FROM seen_jobs WHERE url = ?", (url,)).fetchone()
    return row is not None


def mark_seen(url: str, title: str, source: str) -> None:
    with _connect() as conn:
        conn.execute(
            "INSERT OR IGNORE INTO seen_jobs (url, title, source) VALUES (?, ?, ?)",
            (url, title, source),
        )
