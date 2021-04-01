from dataclasses import dataclass
from datetime import datetime
from typing import List

from .fixtures import fixture_entries


@dataclass
class Entry:
    timestamp: datetime
    description: str
    domain: str  # 'web2', 'web3', or other descriptor
    tags: List[str]
    effort_minutes: int

    def day(self):
        return self.timestamp.date()

    def short_line(self):
        at = self.timestamp.strftime("%Y-%m-%d %H:%M")
        return f"{at} [{self.domain}] {self.description} — {self.effort_minutes}m"


def sample_daybook() -> List[Entry]:
    anchor = datetime(2021, 3, 26, 20, 15)
    return [Entry(**payload) for payload in fixture_entries(anchor)]
