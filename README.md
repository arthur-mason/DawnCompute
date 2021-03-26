# AuroraLedger

AuroraLedger is a solo desktop toolkit that tracks effort on everyday web2 chores while keeping an eye on occasional web3 experiments. It works like a personal journal for side projects, combining payment-ledger style entries with crypto-inspired observability for hobby deployments.

## Why this project

I needed a single place to note what I do after work — sometimes pushing updates to a web2 service, sometimes minting a small NFT idea. AuroraLedger keeps those moments together, so every byte of progress shows up on the same timeline.

## Core concepts

- **Dual-domain entries**: Each log item flags whether it represents a traditional web2 task (deploying a recording server, paying for a plugin) or a web3 experiment (minting a token, inspecting a contract log).
- **Daybook feed**: A lightweight CLI view that groups entries by day and highlights finishing tasks alongside learning notes.
- **Micro-insights**: Summary helpers that count the last seven days of work, split by domain, and surface how much bandwidth is spent chasing downloads vs. chasing chains.

## Architecture

1. `auroraledger.core` houses the `Entry` model plus builders for synthetic entries in a dev journal.
2. `auroraledger.insights` contains functions that compute daily tallies and simple ratios for the daybook feed.
3. `run.py` wires everything together; it simulates a quick batch of entries and prints a human-friendly recap.

## Next steps

- Hook up a file-based store and allow the CLI to append real entries instead of using the built-in sample list.
- Add a thin web frontend that visualizes the ratio of time spent on web2 vs web3 experiments.
- Archive daily snapshots automatically so the log can be reviewed week by week.
