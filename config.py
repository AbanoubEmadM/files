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
        "sre intern",
        "site reliability intern",
        "infrastructure intern",
        "systems engineer intern",
        "linux administrator",
    ],
    "networking": [
        "network engineer intern",
        "network administrator intern",
        "noc engineer",
        "ccna",
        "network support intern",
        "junior network engineer",
        "network analyst intern",
        "network security intern",
        "noc intern",
        "telecom intern",
        "network operations intern",
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
        "desktop support intern",
        "service desk intern",
        "systems administrator intern",
        "endpoint management intern",
    ],
    "cybersecurity": [
        "cybersecurity intern",
        "cyber security intern",
        "information security intern",
        "infosec intern",
        "soc analyst",
        "soc analyst intern",
        "security analyst intern",
        "junior security analyst",
        "threat intelligence intern",
        "vulnerability management intern",
        "penetration testing intern",
        "security operations intern",
    ],
    "cloud_devops": [
        "cloud engineer intern",
        "devops engineer intern",
        "cloud infrastructure intern",
        "platform engineer intern",
        "aws intern",
        "azure intern",
    ],
}
# A posting must contain at least one of these.
ENTRY_LEVEL_KEYWORDS = [
    # General early career
    "intern", "internship", "trainee", "training", "graduate",
    "junior", "entry level", "entry-level", "fresh", "associate",
    # Work-study & regional terms
    "co-op", "coop", "working student", "apprentice", "apprenticeship",
    "early career", "fellowship", "fellow", "student",
    # Technical level qualifiers
    "tier 1", "tier-1", "t1", "level 1", "l1", "first line", "1st line",
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
