"""Generate risk-linkage charts from the concentration-risk panel.

Run from repository root after risk metrics have been generated:
    python scripts/generate_risk_linkage_charts.py

Input:
    data/processed/concentration_risk_panel.csv

Outputs:
    outputs/charts/risk_volatility_by_index.png
    outputs/charts/risk_drawdown_by_index.png
    outputs/charts/concentration_vs_volatility.png
    outputs/charts/concentration_vs_drawdown.png
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "processed" / "concentration_risk_panel.csv"
CHART_DIR = ROOT / "outputs" / "charts"


def load_panel() -> pd.DataFrame:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Missing input file: {INPUT_FILE}")
    return pd.read_csv(INPUT_FILE)


def bar_chart(df: pd.DataFrame, value_col: str, title: str, ylabel: str, filename: str) -> None:
    plot_df = df.dropna(subset=[value_col]).sort_values(value_col, ascending=False)
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


def scatter_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str,
    xlabel: str,
    ylabel: str,
    filename: str,
) -> None:
    plot_df = df.dropna(subset=[x_col, y_col])
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(plot_df[x_col], plot_df[y_col])
    for _, row in plot_df.iterrows():
        ax.annotate(str(row["index_id"]), (row[x_col], row[y_col]), fontsize=8, xytext=(5, 5), textcoords="offset points")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.tight_layout()
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(CHART_DIR / filename, dpi=200)
    plt.close(fig)


def main() -> None:
    df = load_panel()
    bar_chart(
        df,
        "annualized_volatility",
        "Annualized Volatility by Index",
        "Annualized Volatility",
        "risk_volatility_by_index.png",
    )
    bar_chart(
        df,
        "maximum_drawdown",
        "Maximum Drawdown by Index",
        "Maximum Drawdown",
        "risk_drawdown_by_index.png",
    )
    scatter_chart(
        df,
        "hhi_percent_points",
        "annualized_volatility",
        "Concentration vs Annualized Volatility",
        "HHI Percent-Points",
        "Annualized Volatility",
        "concentration_vs_volatility.png",
    )
    scatter_chart(
        df,
        "hhi_percent_points",
        "maximum_drawdown",
        "Concentration vs Maximum Drawdown",
        "HHI Percent-Points",
        "Maximum Drawdown",
        "concentration_vs_drawdown.png",
    )
    print("Risk-linkage charts generated.")


if __name__ == "__main__":
    main()
