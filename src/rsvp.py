"""RSVP Manager — Starter

You are cleaning up RSVP emails for an event.

Implement the three functions below without mutating inputs.
"""
from typing import List, Tuple


def dedupe_emails_case_preserve_order(emails: List[str]) -> List[str]:
    """Return a new list with duplicate emails removed, preserving first seen.

    Treat emails case-insensitively ("ALICE@x.com" == "alice@x.com").
    Keep the first form you saw.

    Ignore entries that do not contain an '@' character.
    """
    result = []
    seen = set()
    
    for email in emails:
        if '@' not in email:
            continue
        key = email.lower()
        if key not in seen:
            seen.add(key)
            result.append(email)
    return result
    raise NotImplementedError


def first_with_domain(emails: List[str], domain: str) -> int | None:
    """Return the index of the first email whose domain matches `domain`.

    Examples:
        emails=["a@x.com","b@y.com"], domain="y.com" -> 1
        no match -> None
    Comparison is case-insensitive.
    """
    for i, email in enumerate(emails):
        if '@' not in email:
            continue
        _, email_domain = email.split('@', 1)
        if email_domain.lower() == domain.lower():
            return i
    return None
    raise NotImplementedError


def domain_counts(emails: List[str]) -> List[Tuple[str, int]]:
    """Return (domain, count) pairs sorted by domain (A..Z), case-insensitive.

    Skip malformed entries without an '@'.
    Example: ["a@x.com","b@x.com","c@y.com"] -> [("x.com", 2), ("y.com", 1)]
    """
    counts = {}
    for email in emails:
        if '@' not in email:
            continue
        _, domain = email.split('@', 1)
        domain = domain.lower()
        counts[domain] = counts.get(domain, 0) + 1
    
    return sorted(counts.items(), key=lambda x: x[0])
    raise NotImplementedError