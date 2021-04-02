from typing import Iterable, List, Optional

from .core import Entry, sample_daybook


class DaybookStore:
    """In-memory collection of daybook entries with simple filters."""

    def __init__(self, entries: Iterable[Entry]) -> None:
        self._entries = list(entries)

    @classmethod
    def from_sample(cls) -> "DaybookStore":
        return cls(sample_daybook())

    def all_entries(self) -> List[Entry]:
        return list(self._entries)

    def filter_by_domain(self, domain: Optional[str] = None) -> List[Entry]:
        if domain is None:
            return self.all_entries()
        return [entry for entry in self._entries if entry.domain == domain]

    def total_minutes(self, domain: Optional[str] = None) -> int:
        return sum(entry.effort_minutes for entry in self.filter_by_domain(domain))

    def tags_for_domain(self, domain: str) -> List[str]:
        tags = []
        for entry in self.filter_by_domain(domain):
            tags.extend(entry.tags)
        return sorted(set(tags))
