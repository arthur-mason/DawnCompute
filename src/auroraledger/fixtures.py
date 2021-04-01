from datetime import datetime, timedelta
from typing import Iterable, Dict


def fixture_entries(anchor: datetime) -> Iterable[Dict]:
    offsets = [
        (2, 3, 12, "Reviewed new analytics UI mock for the web2 dashboard", "web2", ["ui", "analytics"], 40),
        (2, 1, 5, "Logged a concept for a web3 snapshot hook and its gas budget", "web3", ["concept", "gas"], 25),
        (1, 4, 25, "Tuned the payment reminder cron job backoff strategy", "web2", ["ops", "cron"], 35),
        (1, 1, 40, "Ran through the web3 wallet sync after connecting new RPC", "web3", ["node", "wallet"], 20),
        (0, 5, 18, "Drafted README notes for AuroraLedger's second chapter", "web2", ["docs"], 45),
        (0, 2, 7, "Checked on the mint simulator status feed", "web3", ["mint", "sim"], 15),
    ]
    for days, hours, minutes, description, domain, tags, effort in offsets:
        yield {
            "timestamp": anchor - timedelta(days=days, hours=hours, minutes=minutes),
            "description": description,
            "domain": domain,
            "tags": tags,
            "effort_minutes": effort,
        }
