"""Visualization helpers for index concentration analysis."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def plot_hhi_trend(df: pd.DataFrame, index_name: str):
    """Plot HHI over time for a selected index."""
    subset = df[df["index_name"] == index_name].copy()
    subset["snapshot_date"] = pd.to_datetime(subset["snapshot_date"])
    subset = subset.sort_values("snapshot_date")

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(subset["snapshot_date"], subset["hhi"], marker="o")
    ax.set_title(f"HHI Trend: {index_name}")
    ax.set_xlabel("Date")
    ax.set_ylabel("HHI")
    fig.tight_layout()
    return fig, ax


def plot_top_weight_trend(df: pd.DataFrame, index_name: str):
    """Plot Top-3, Top-5, and Top-10 weight trends for a selected index."""
    subset = df[df["index_name"] == index_name].copy()
    subset["snapshot_date"] = pd.to_datetime(subset["snapshot_date"])
    subset = subset.sort_values("snapshot_date")

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(subset["snapshot_date"], subset["top3_weight"], marker="o", label="Top 3")
    ax.plot(subset["snapshot_date"], subset["top5_weight"], marker="o", label="Top 5")
    ax.plot(subset["snapshot_date"], subset["top10_weight"], marker="o", label="Top 10")
    ax.set_title(f"Top-Constituent Weight Trend: {index_name}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Combined Weight")
    ax.legend()
    fig.tight_layout()
    return fig, ax


def plot_effective_n_comparison(df: pd.DataFrame):
    """Plot latest effective-N comparison across indices."""
    latest = df.sort_values("snapshot_date").groupby("index_name").tail(1)
    latest = latest.sort_values("effective_n")

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(latest["index_name"], latest["effective_n"])
    ax.set_title("Latest Effective Number of Stocks by Index")
    ax.set_xlabel("Index")
    ax.set_ylabel("Effective N")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig, ax
