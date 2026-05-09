"""Generate current-snapshot tables and charts from concentration metrics.

Run from repository root:
    python scripts/generate_current_snapshot_outputs.py

Inputs:
    data/processed/concentration_metrics.csv

Outputs:
    outputs/tables/current_snapshot_concentration_summary.csv
    outputs/charts/current_snapshot_top10_weight.png
    outputs/charts/current_snapshot_hhi_percent_points.png
    outputs/charts/current_snapshot_effective_n.png
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "processed" / "concentration_metrics.csv"
TABLE_DIR = ROOT / "outputs" / "tables"
CHART_DIR = ROOT / "outputs" / "charts"


def load_data() -> pd.DataFrame:
    df = pd.read_csv(INPUT_FILE)
    df["snapshot_date"] = pd.to_datetime(df["snapshot_date"], errors="coerce")
    return df


def write_summary_table(df: pd.DataFrame) -> None:
    cols = [
        "index_id",
        "index_name",
        "snapshot_date",
        "coverage_type",
        "top3_weight_percent",
        "top5_weight_percent",
        "top10_weight_percent",
        "hhi_percent_points",
        "effective_n",
        "sector_hhi_percent_points",
        "data_quality_flag",
    ]
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    df[cols].to_csv(TABLE_DIR / "current_snapshot_concentration_summary.csv", index=False)


def _bar_chart(df: pd.DataFrame, value_col: str, title: str, ylabel: str, filename: str) -> None:
    plot_df = df.sort_values(value_col, ascending=False).copy()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(plot_df["index_name"], plot_df[value_col])
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Index")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(CHART_DIR / filename, dpi=200)
    plt.close(fig)


def main() -> None:
    df = load_data()
    write_summary_table(df)
    _bar_chart(
        df,
        "top10_weight_percent",
        "Current Snapshot: Top-10 Constituent Weight by Index",
        "Top-10 Weight (%)",
        "current_snapshot_top10_weight.png",
    )
    _bar_chart(
        df,
        "hhi_percent_points",
        "Current Snapshot: HHI Percent-Points by Index",
        "HHI Percent-Points",
        "current_snapshot_hhi_percent_points.png",
    )
    _bar_chart(
        df,
        "effective_n",
        "Current Snapshot: Effective Number of Stocks by Index",
        "Effective N",
        "current_snapshot_effective_n.png",
    )
    print("Current snapshot outputs generated.")


if __name__ == "__main__":
    main()
