# Egypt IT Internship Alert Bot

Checks Wuzzuf and Forasna for Linux, networking, and sysadmin internships in Egypt, and sends new matches to your Telegram.

## 1. Create a Telegram bot

1. Open Telegram and message **@BotFather**.
2. Send `/newbot`, follow the prompts, and copy the **bot token**. 8986593983:AAHqxiujanP6y0iE32lOlbEV5oeMB07pGwI
3. Open a chat with your new bot and send it any message (e.g., "hi").
4. In a browser, open `https://api.telegram.org/bot8986593983:AAHqxiujanP6y0iE32lOlbEV5oeMB07pGwI/getUpdates`.
5. Find `"chat":{"id": 1256277220...}` in the response. That number is your **chat ID**.

## 2. Test locally

```bash
cd internship-bot
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

export TELEGRAM_BOT_TOKEN="8986593983:AAHqxiujanP6y0iE32lOlbEV5oeMB07pGwI"
export TELEGRAM_CHAT_ID="your-chat-id"
python main.py
```

Read the log output. It shows how many postings each source returned. If a source shows 0, open that site's search page in your browser, right-click a job title, and copy the link's URL. Make sure the `link_pattern` in `scrapers.py` matches part of that URL.

## 3. Run it automatically on GitHub (free)

1. Create a new GitHub repository and push this folder to it.
2. Go to **Settings → Secrets and variables → Actions** and add:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
3. Go to the **Actions** tab, select "Check internships", and click **Run workflow** to test it.
4. After that it runs every 3 hours on its own.

## Notes

- **First run:** Every current matching posting counts as new, so you may get up to 25 messages at once. The rest arrive on later runs.
- **Duplicates:** Each job URL is stored in `seen_jobs.db`, so you only get alerted once per posting.
- **Scraping etiquette:** The bot waits 2 seconds between requests and identifies itself. Check each site's terms of service before running it often, and keep the interval at a few hours.
- **Site changes:** Job sites change their HTML from time to time. If alerts stop, check the log first.
- **Tuning:** Edit `config.py` to add search terms, keywords, or locations.

## Adding a source later

1. Add an entry to `SOURCES` in `scrapers.py` with the site's search URL and a `link_pattern` that matches its job-detail links.
2. Run `python main.py` and confirm the source returns results.
