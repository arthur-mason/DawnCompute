"""Tiny CLI helper for exploring the daybook."""

from argparse import ArgumentParser
from typing import Iterable

from .insights import render_daybook
from .store import DaybookStore


def main(args: Iterable[str] | None = None) -> None:
    parser = ArgumentParser(description="AuroraLedger daybook quick viewer")
    parser.add_argument("--domain", choices=["web2", "web3"], help="Limit output to a single domain", default=None)
    parsed = parser.parse_args(args)
    store = DaybookStore.from_sample()
    entries = store.filter_by_domain(parsed.domain)
    print(render_daybook(entries))


if __name__ == "__main__":
    main()
