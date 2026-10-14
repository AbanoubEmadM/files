# config.py
# Edit these lists to tune what the bot looks for.

SEARCH_TERMS = {
    "linux_sysadmin": [
        "linux system administrator",
        "linux intern",
        "sysadmin intern",
        "junior linux",
        "IT Intern",
        "system administrator intern",
        "devops intern",
    ],
    "networking": [
        "network engineer intern",
        "network administrator intern",
        "noc engineer",
        "ccna",
        "network support intern",
        "junior network engineer",
    ],
    "windows_sysadmin": [
        "windows server administrator",
        "active directory intern",
        "windows system administrator intern",
        "it support intern",
        "IT Intern",
        "it help desk",
        "help desk",
        "junior windows administrator",
    ],
    "cybersecurity": [
        "soc analyst"
    ]
}

# A posting must contain at least one of these.
ENTRY_LEVEL_KEYWORDS = [
    "intern", "internship", "trainee", "training", "graduate",
    "junior", "entry level", "entry-level", "fresh", "associate",
]

# A posting containing any of these is dropped.
EXCLUDE_KEYWORDS = [
    "senior", "lead", "principal", "manager", "head of",
    "5+ years", "5 years", "7+ years", "architect", "3+ years"
]

# A posting must mention one of these locations, or Remote/Hybrid.
LOCATIONS = ["cairo", "giza", "6th of october", "new cairo", "remote", "hybrid", "egypt"]

# Politeness delay between HTTP requests, in seconds.
REQUEST_DELAY = 2

# Maximum alerts sent in a single run, so a first run doesn't flood your chat.
MAX_ALERTS_PER_RUN = 25
