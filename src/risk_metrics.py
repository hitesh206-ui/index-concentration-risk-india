"""Risk metric functions for index concentration analysis."""

from __future__ import annotations

import math

import numpy as np
import pandas as pd


def simple_returns(price_series: pd.Series) -> pd.Series:
    """Compute simple returns from an index level or price series."""
    return price_series.astype(float).pct_change()


def log_returns(price_series: pd.Series) -> pd.Series:
    """Compute log returns from an index level or price series."""
    prices = price_series.astype(float)
    return np.log(prices / prices.shift(1))


def annualized_volatility(returns: pd.Series, periods_per_year: int = 12) -> float:
    """Compute annualized volatility from periodic returns."""
    clean = returns.dropna().astype(float)
    if clean.empty:
        return math.nan
    return float(clean.std(ddof=1) * math.sqrt(periods_per_year))


def drawdown(index_level: pd.Series) -> pd.Series:
    """Compute drawdown series from an index level series."""
    levels = index_level.astype(float)
    running_max = levels.cummax()
    return levels / running_max - 1


def maximum_drawdown(index_level: pd.Series) -> float:
    """Compute maximum drawdown from an index level series."""
    dd = drawdown(index_level)
    if dd.dropna().empty:
        return math.nan
    return float(dd.min())


def rolling_volatility(
    returns: pd.Series,
    window: int = 12,
    periods_per_year: int = 12,
) -> pd.Series:
    """Compute rolling annualized volatility."""
    return returns.rolling(window).std() * math.sqrt(periods_per_year)


def risk_summary(
    df: pd.DataFrame,
    index_level_col: str = "index_level",
    group_cols: list[str] | None = None,
    date_col: str = "date",
    periods_per_year: int = 12,
) -> pd.DataFrame:
    """Compute risk metrics by index.

    Expected input columns include index identifier columns, date, and index level.
    """
    if group_cols is None:
        group_cols = ["index_id", "index_name"]

    rows = []
    for keys, group in df.groupby(group_cols, dropna=False):
        if not isinstance(keys, tuple):
            keys = (keys,)
        g = group.sort_values(date_col).copy()
        returns = simple_returns(g[index_level_col])
        row = {col: key for col, key in zip(group_cols, keys)}
        row.update(
            {
                "observation_count": int(g[index_level_col].dropna().shape[0]),
                "start_date": g[date_col].min(),
                "end_date": g[date_col].max(),
                "mean_periodic_return": float(returns.mean()) if not returns.dropna().empty else math.nan,
                "annualized_volatility": annualized_volatility(returns, periods_per_year),
                "maximum_drawdown": maximum_drawdown(g[index_level_col]),
            }
        )
        rows.append(row)
    return pd.DataFrame(rows)
