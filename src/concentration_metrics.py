"""Concentration metric functions for equity index analysis.

The workbook reports both decimal-scale HHI and percent-points HHI.
This module follows the same convention.
"""

from __future__ import annotations

import math
from typing import Iterable

import numpy as np
import pandas as pd


def _to_decimal_weights(weights: Iterable[float], weights_are_percent: bool = True) -> np.ndarray:
    """Convert weights into decimal form and drop missing values."""
    arr = np.array(list(weights), dtype=float)
    arr = arr[~np.isnan(arr)]
    if weights_are_percent:
        arr = arr / 100.0
    return arr


def hhi_decimal(weights: Iterable[float], weights_are_percent: bool = True) -> float:
    """Calculate decimal-scale HHI: sum((weight_decimal)^2)."""
    w = _to_decimal_weights(weights, weights_are_percent)
    return float(np.sum(w ** 2))


def hhi_percent_points(weights: Iterable[float], weights_are_percent: bool = True) -> float:
    """Calculate HHI in percent-points squared.

    Example: decimal HHI of 0.05 becomes 500.0.
    """
    return float(hhi_decimal(weights, weights_are_percent) * 10000)


def effective_n(weights: Iterable[float], weights_are_percent: bool = True) -> float:
    """Calculate effective number of equally weighted constituents."""
    value = hhi_decimal(weights, weights_are_percent)
    if value == 0:
        return math.nan
    return float(1 / value)


def top_n_weight_percent(weights: Iterable[float], n: int, weights_are_percent: bool = True) -> float:
    """Calculate combined top-N weight in percentage units."""
    w = _to_decimal_weights(weights, weights_are_percent)
    if w.size == 0:
        return math.nan
    return float(np.sort(w)[::-1][:n].sum() * 100)


def shannon_entropy(weights: Iterable[float], weights_are_percent: bool = True) -> float:
    """Calculate Shannon entropy: -sum(w * ln(w)).

    Shannon entropy rises as weights become more diversified.
    """
    w = _to_decimal_weights(weights, weights_are_percent)
    w = w[w > 0]
    if w.size == 0:
        return math.nan
    return float(-np.sum(w * np.log(w)))


def theil_concentration(weights: Iterable[float], weights_are_percent: bool = True) -> float:
    """Calculate Theil-style concentration: ln(N) - Shannon entropy.

    Higher values indicate greater concentration / inequality.
    """
    w = _to_decimal_weights(weights, weights_are_percent)
    w = w[w > 0]
    if w.size == 0:
        return math.nan
    return float(np.log(len(w)) - shannon_entropy(w, weights_are_percent=False))


def concentration_summary(
    df: pd.DataFrame,
    weight_col: str = "weight_percent",
    group_cols: list[str] | None = None,
    weights_are_percent: bool = True,
) -> pd.DataFrame:
    """Compute concentration metrics by index/date or other groups."""
    if group_cols is None:
        group_cols = ["index_id", "index_name", "snapshot_date"]

    rows = []
    for keys, group in df.groupby(group_cols, dropna=False):
        if not isinstance(keys, tuple):
            keys = (keys,)
        weights = group[weight_col].dropna().astype(float).tolist()
        row = {col: key for col, key in zip(group_cols, keys)}
        row.update(
            {
                "constituent_count": len(weights),
                "weight_sum_percent": float(np.sum(weights)) if weights_are_percent else float(np.sum(weights) * 100),
                "hhi_decimal": hhi_decimal(weights, weights_are_percent),
                "hhi_percent_points": hhi_percent_points(weights, weights_are_percent),
                "effective_n": effective_n(weights, weights_are_percent),
                "top3_weight_percent": top_n_weight_percent(weights, 3, weights_are_percent),
                "top5_weight_percent": top_n_weight_percent(weights, 5, weights_are_percent),
                "top10_weight_percent": top_n_weight_percent(weights, 10, weights_are_percent),
                "shannon_entropy": shannon_entropy(weights, weights_are_percent),
                "theil_concentration": theil_concentration(weights, weights_are_percent),
            }
        )
        rows.append(row)

    return pd.DataFrame(rows)


def sector_concentration_summary(
    df: pd.DataFrame,
    sector_weight_col: str = "sector_weight_percent",
    group_cols: list[str] | None = None,
    weights_are_percent: bool = True,
) -> pd.DataFrame:
    """Compute sector HHI metrics by index/date."""
    if group_cols is None:
        group_cols = ["index_id", "index_name", "snapshot_date"]

    rows = []
    for keys, group in df.groupby(group_cols, dropna=False):
        if not isinstance(keys, tuple):
            keys = (keys,)
        weights = group[sector_weight_col].dropna().astype(float).tolist()
        row = {col: key for col, key in zip(group_cols, keys)}
        row["sector_hhi_decimal"] = hhi_decimal(weights, weights_are_percent)
        row["sector_hhi_percent_points"] = hhi_percent_points(weights, weights_are_percent)
        rows.append(row)
    return pd.DataFrame(rows)
