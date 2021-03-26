from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List


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
    entries = [
        Entry(
            timestamp=anchor - timedelta(days=2, hours=3, minutes=12),
            description="Reviewed new analytics UI mock for the web2 dashboard",
            domain="web2",
            tags=["ui", "analytics"],
            effort_minutes=40,
        ),
        Entry(
            timestamp=anchor - timedelta(days=2, hours=1, minutes=5),
            description="Logged a concept for a web3 snapshot hook and its gas budget",
            domain="web3",
            tags=["concept", "gas"],
            effort_minutes=25,
        ),
        Entry(
            timestamp=anchor - timedelta(days=1, hours=4, minutes=25),
            description="Tuned the payment reminder cron job backoff strategy",
            domain="web2",
            tags=["ops", "cron"],
            effort_minutes=35,
        ),
        Entry(
            timestamp=anchor - timedelta(days=1, hours=1, minutes=40),
            description="Ran through the web3 wallet sync after connecting new RPC",
            domain="web3",
            tags=["node", "wallet"],
            effort_minutes=20,
        ),
        Entry(
            timestamp=anchor - timedelta(hours=5, minutes=18),
            description="Drafted README notes for AuroraLedger's second chapter",
            domain="web2",
            tags=["docs"],
            effort_minutes=45,
        ),
        Entry(
            timestamp=anchor - timedelta(hours=2, minutes=7),
            description="Checked on the mint simulator status feed",
            domain="web3",
            tags=["mint", "sim"],
            effort_minutes=15,
        ),
    ]
    return entries
