"""Concentration metric functions for equity index analysis."""

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


def hhi(weights: Iterable[float], weights_are_percent: bool = True) -> float:
    """Calculate Herfindahl-Hirschman Index from constituent weights."""
    w = _to_decimal_weights(weights, weights_are_percent)
    return float(np.sum(w ** 2))


def effective_n(weights: Iterable[float], weights_are_percent: bool = True) -> float:
    """Calculate effective number of equally weighted constituents."""
    value = hhi(weights, weights_are_percent)
    if value == 0:
        return math.nan
    return float(1 / value)


def top_n_weight(weights: Iterable[float], n: int, weights_are_percent: bool = True) -> float:
    """Calculate the combined weight of the largest N constituents."""
    w = _to_decimal_weights(weights, weights_are_percent)
    if w.size == 0:
        return math.nan
    return float(np.sort(w)[::-1][:n].sum())


def theil_entropy(weights: Iterable[float], weights_are_percent: bool = True) -> float:
    """Calculate a Theil-style inequality metric for index weights.

    A perfectly equal-weighted index has value near 0. Higher values indicate
    greater weight inequality.
    """
    w = _to_decimal_weights(weights, weights_are_percent)
    w = w[w > 0]
    if w.size == 0:
        return math.nan
    mean_w = np.mean(w)
    return float(np.mean((w / mean_w) * np.log(w / mean_w)))


def concentration_summary(
    df: pd.DataFrame,
    weight_col: str = "weight",
    group_cols: list[str] | None = None,
    weights_are_percent: bool = True,
) -> pd.DataFrame:
    """Compute concentration metrics by index/date or other groups.

    Parameters
    ----------
    df:
        Dataframe containing constituent weights.
    weight_col:
        Column containing constituent weights.
    group_cols:
        Grouping columns, e.g. ["index_name", "snapshot_date"].
    weights_are_percent:
        True if weights are in percent units, e.g. 13.63 for 13.63%.
    """
    if group_cols is None:
        group_cols = ["index_name", "snapshot_date"]

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
                "hhi": hhi(weights, weights_are_percent),
                "effective_n": effective_n(weights, weights_are_percent),
                "top3_weight": top_n_weight(weights, 3, weights_are_percent),
                "top5_weight": top_n_weight(weights, 5, weights_are_percent),
                "top10_weight": top_n_weight(weights, 10, weights_are_percent),
                "theil_entropy": theil_entropy(weights, weights_are_percent),
            }
        )
        rows.append(row)

    return pd.DataFrame(rows)


def sector_hhi(df: pd.DataFrame, sector_weight_col: str = "sector_weight", weights_are_percent: bool = True) -> float:
    """Calculate HHI from sector-level weights."""
    return hhi(df[sector_weight_col], weights_are_percent=weights_are_percent)
