# Poker Now Ledger & EV Calculator

A Python analytics pipeline that processes Poker Now hand history and ledger exports to compute player balances, estimate all-in expected value (EV), and visualize performance across sessions. The project automates post-session analysis, enabling players to understand variance, track profitability, and identify long-term trends.

---

## Overview

Poker Now Ledger & EV Calculator converts raw Poker Now CSV exports into structured financial summaries and EV-based performance analytics.

The system:

- Parses hand history logs to detect all-in situations
- Extracts showdown cards and pot distributions
- Computes exact or simulated equity for each all-in
- Aggregates player results relative to EV
- Generates cumulative run-good / run-bad visualizations
- Processes ledger exports to produce overall financial summaries

A lookup-table caching system is used to dramatically accelerate repeated equity computations.

---

## Features

### Hand History Processing
- Automated parsing of Poker Now log exports
- Detection of all-in events and board state
- Extraction of player hole cards and pot collection

### Equity & EV Computation
- Exact combinatorial equity calculation for postflop all-ins
- Monte Carlo simulation support for preflop scenarios
- Canonicalized lookup table to cache equity results
- Automatic persistence of computed equities

### Ledger Aggregation
- Multi-session ledger ingestion
- Player ID → display name mapping
- Net result aggregation across sessions

### Visualization
- Interactive Plotly run-good / run-bad graphs
- Cumulative EV vs actual tracking
- Multi-player comparison plots
- Exportable HTML visualizations

---

## Tech Stack

- Python
- Pandas (data ingestion & transformation)
- Treys poker evaluation engine
- Plotly (interactive visualization)
- JSON lookup caching
- Regular expressions for log parsing

---

## Project Structure

```
poker-now-ledger/
│
├── ev_graphs.py          # All-in EV computation & visualization
├── player_results.py     # Ledger aggregation & summaries
├── equity_lookup.json    # Cached equity lookup table (generated)
├── data/                 # Poker Now logs & ledgers (optional / ignored)
├── outputs/              # Generated graphs & reports
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone repository

```
git clone https://github.com/your-username/poker-now-ledger.git
cd poker-now-ledger
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # macOS / Linux
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add Poker Now exports

Place Poker Now CSV logs and ledger files inside a `data/` directory or adjust paths within scripts.

### 5. Run EV analysis

```
python ev_graphs.py
```

This generates:

- Console summary of player EV performance
- Interactive Plotly graph (`ev_graphs.html`)
- Updated equity lookup cache

### 6. Run ledger aggregation

```
python player_results.py
```

This produces aggregated financial results across sessions.

---

## Example Outputs

- Cumulative run-good / run-bad graphs
- Player EV leaderboards
- Multi-session ledger summaries
- Interactive HTML visualizations

Screenshots:
![EV Graph](assets/ev_graph.png)

---

## Motivation

Poker results are heavily influenced by short-term variance, especially in all-in situations. Manual analysis is tedious and often inaccurate.

This project was created to:

- Automate EV-based performance analysis
- Quantify variance across sessions
- Provide transparent ledger tracking
- Build a reusable poker analytics framework

---

## License

This project is licensed under the MIT License.

## Author

Shaan Cheruvu
https://github.com/Shaan50
