"""Run index return and risk metric calculations.

Usage from repository root:

    python scripts/run_risk_metrics.py

Input:
    data/processed/index_returns.csv

Output:
    data/processed/risk_metrics.csv

Expected input columns:
    index_id,index_name,date,index_level
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.risk_metrics import simple_returns, drawdown, rolling_volatility, risk_summary


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed"
INPUT_FILE = DATA_DIR / "index_returns.csv"
OUTPUT_FILE = DATA_DIR / "risk_metrics.csv"
ENRICHED_FILE = DATA_DIR / "index_returns_enriched.csv"


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)
    required = {"index_id", "index_name", "date", "index_level"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df = df.dropna(subset=["index_id", "index_name", "date", "index_level"]).copy()
    df["date"] = pd.to_datetime(df["date"])
    df["index_level"] = pd.to_numeric(df["index_level"], errors="coerce")
    df = df.dropna(subset=["index_level"])
    df = df.sort_values(["index_id", "date"])

    enriched = []
    for _, group in df.groupby("index_id", dropna=False):
        g = group.sort_values("date").copy()
        g["periodic_return"] = simple_returns(g["index_level"])
        g["drawdown"] = drawdown(g["index_level"])
        g["rolling_12m_volatility"] = rolling_volatility(g["periodic_return"], window=12, periods_per_year=12)
        enriched.append(g)

    enriched_df = pd.concat(enriched, ignore_index=True) if enriched else pd.DataFrame()
    risk_df = risk_summary(df, index_level_col="index_level", group_cols=["index_id", "index_name"], date_col="date")

    ENRICHED_FILE.parent.mkdir(parents=True, exist_ok=True)
    enriched_df.to_csv(ENRICHED_FILE, index=False)
    risk_df.to_csv(OUTPUT_FILE, index=False)

    print(f"Wrote enriched returns to {ENRICHED_FILE}")
    print(f"Wrote risk metrics to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
