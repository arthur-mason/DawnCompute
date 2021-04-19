"""A quick script to dump daybook highlights for the week."""

from auroraledger.insights import render_daybook
from auroraledger.store import DaybookStore


def main() -> None:
    store = DaybookStore.from_sample()
    print("=== AuroraLedger quick report ===")
    print(render_daybook(store.all_entries()))
    print("\nDomain focus")
    for domain in ("web2", "web3"):
        print(f"{domain} entries: {len(store.filter_by_domain(domain))}, {store.total_minutes(domain)}m total")
        if domain == "web3":
            print(f"  tags: {', '.join(store.tags_for_domain(domain))}")


if __name__ == "__main__":
    main()
