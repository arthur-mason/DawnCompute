"""Entry script for the AuroraLedger daybook."""

from auroraledger.core import sample_daybook
from auroraledger.insights import render_daybook


def main() -> None:
    daybook = sample_daybook()
    summary = render_daybook(daybook)
    print(summary)


if __name__ == "__main__":
    main()
