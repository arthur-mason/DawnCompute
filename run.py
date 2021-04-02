"""Entry script for the AuroraLedger daybook."""

from auroraledger.insights import render_daybook
from auroraledger.store import DaybookStore


def main() -> None:
    store = DaybookStore.from_sample()
    summary = render_daybook(store.all_entries())
    print(summary)
    print("\nQuick check")
    for domain in ("web2", "web3"):
        minutes = store.total_minutes(domain)
        tags = ", ".join(store.tags_for_domain(domain))
        print(f"- {domain}: {minutes} minutes; tags: {tags}")


if __name__ == "__main__":
    main()
