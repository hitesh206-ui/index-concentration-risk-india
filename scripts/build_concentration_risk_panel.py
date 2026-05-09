"""Build a concentration-risk panel by merging concentration and risk metrics.

Usage from repository root:

    python scripts/build_concentration_risk_panel.py

Inputs:
    data/processed/concentration_metrics.csv
    data/processed/risk_metrics.csv

Output:
    data/processed/concentration_risk_panel.csv
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed"
CONCENTRATION_FILE = DATA_DIR / "concentration_metrics.csv"
RISK_FILE = DATA_DIR / "risk_metrics.csv"
OUTPUT_FILE = DATA_DIR / "concentration_risk_panel.csv"


def main() -> None:
    if not CONCENTRATION_FILE.exists():
        raise FileNotFoundError(f"Missing input: {CONCENTRATION_FILE}")
    if not RISK_FILE.exists():
        raise FileNotFoundError(f"Missing input: {RISK_FILE}")

    concentration = pd.read_csv(CONCENTRATION_FILE)
    risk = pd.read_csv(RISK_FILE)

    required_conc = {"index_id", "index_name"}
    required_risk = {"index_id", "index_name"}
    missing_conc = required_conc - set(concentration.columns)
    missing_risk = required_risk - set(risk.columns)

    if missing_conc:
        raise ValueError(f"Concentration metrics missing columns: {sorted(missing_conc)}")
    if missing_risk:
        raise ValueError(f"Risk metrics missing columns: {sorted(missing_risk)}")

    # For a first-stage panel, merge latest concentration snapshot with full-period risk metrics.
    # Later versions can use rolling-window risk metrics matched by snapshot date.
    if "snapshot_date" in concentration.columns:
        concentration["snapshot_date"] = pd.to_datetime(concentration["snapshot_date"], errors="coerce")
        latest_concentration = (
            concentration.sort_values("snapshot_date")
            .groupby("index_id", dropna=False)
            .tail(1)
        )
    else:
        latest_concentration = concentration.copy()

    panel = latest_concentration.merge(
        risk,
        on=["index_id", "index_name"],
        how="left",
        suffixes=("", "_risk"),
    )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    panel.to_csv(OUTPUT_FILE, index=False)
    print(f"Wrote {len(panel)} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
