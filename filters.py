# filters.py
import re

from config import ENTRY_LEVEL_KEYWORDS, EXCLUDE_KEYWORDS, LOCATIONS


def _has_word(text: str, word: str) -> bool:
    # Whole-word match, so "lead" doesn't match "leadership" or "leading".
    return re.search(rf"\b{re.escape(word)}\b", text) is not None


def relevance_reason(title: str, description: str, location: str = "") -> str:
    """Return 'ok' if the job passes, otherwise the reason it was rejected."""
    text = f"{title} {description} {location}".lower()

    for word in EXCLUDE_KEYWORDS:
        if _has_word(text, word.lower()):
            return f"excluded by '{word}'"

    if not any(_has_word(text, word.lower()) for word in ENTRY_LEVEL_KEYWORDS):
        return "no entry-level keyword"

    if not any(place.lower() in text for place in LOCATIONS):
        return "no location match"

    return "ok"


def is_relevant(title: str, description: str, location: str = "") -> bool:
    return relevance_reason(title, description, location) == "ok"