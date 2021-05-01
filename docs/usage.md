# Usage notes for AuroraLedger

## CLI run script

- `python run.py` boots the daybook runner that uses `DaybookStore` and `render_daybook` to present a chronological log plus quick domain summaries.
- The store helper keeps the work feed as an in-memory collection, so the CLI can highlight web2 vs. web3 minutes without hooking up a persistent backend yet.

## Quick report

- `scripts/daybook_report.py` calls the same store and renders an alternate summary, printing both the full timeline and the latest domain counts.
- It is handy when I want to drop a quick note into the local terminal after a long evening of side projects.

## Testing

- `tests/test_insights.py` covers the core totals, daybook rendering, and store helpers so I can see how the modules behave as I build new entries.
- Running `pytest` (once I set up a virtualenv) should keep these modules honest before a commit.
