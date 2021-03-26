from collections import defaultdict
from typing import Iterable, Dict

from .core import Entry


def group_by_day(entries: Iterable[Entry]) -> Dict[str, list]:
    days = defaultdict(list)
    for entry in sorted(entries, key=lambda e: e.timestamp):
        days[entry.day().isoformat()].append(entry)
    return days


def domain_totals(entries: Iterable[Entry]) -> Dict[str, int]:
    totals = defaultdict(int)
    for entry in entries:
        key = entry.domain if entry.domain in ("web2", "web3") else "other"
        totals[key] += entry.effort_minutes
    return totals


def render_daybook(entries: Iterable[Entry]) -> str:
    timeline = ["Daybook"]
    days = group_by_day(entries)
    for day, day_entries in sorted(days.items()):
        timeline.append(f"\n{day}")
        for entry in day_entries:
            timeline.append(f"  • {entry.short_line()}")
    totals = domain_totals(entries)
    timeline.append("\nSummary")
    for domain, minutes in totals.items():
        timeline.append(f"  - {domain}: {minutes} minutes")
    return "\n".join(timeline)
