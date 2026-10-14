# notifier.py
import html
import logging
import os

import requests

log = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")


def send_job_alert(job: dict) -> bool:
    if not BOT_TOKEN or not CHAT_ID:
        log.error("TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID is not set")
        return False

    text = (
        f"<b>New internship</b> ({html.escape(job['source'])})\n"
        f"{html.escape(job['title'])}\n"
        f"{html.escape(job['url'])}"
    )

    try:
        resp = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": CHAT_ID,
                "text": text,
                "parse_mode": "HTML",
                "disable_web_page_preview": False,
            },
            timeout=15,
        )
        resp.raise_for_status()
        return True
    except requests.RequestException as exc:
        log.warning("Telegram send failed: %s", exc)
        return False
