"""Run concentration metric calculations for index constituent and sector weights.

Usage from repository root:

    python scripts/run_concentration_metrics.py

Inputs:
    data/processed/constituent_weights.csv
    data/processed/sector_weights.csv

Output:
    data/processed/concentration_metrics.csv

The script expects weights in percentage units, e.g. 13.63 for 13.63%.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.concentration_metrics import concentration_summary, sector_concentration_summary


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed"
CONSTITUENT_FILE = DATA_DIR / "constituent_weights.csv"
SECTOR_FILE = DATA_DIR / "sector_weights.csv"
OUTPUT_FILE = DATA_DIR / "concentration_metrics.csv"


def _read_csv_if_exists(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    return pd.read_csv(path)


def _validate_constituent_data(df: pd.DataFrame) -> pd.DataFrame:
    required = {
        "index_id",
        "index_name",
        "snapshot_date",
        "constituent_name",
        "weight_percent",
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required constituent columns: {sorted(missing)}")

    clean = df.copy()
    clean = clean.dropna(subset=["index_id", "index_name", "snapshot_date", "weight_percent"])
    clean["weight_percent"] = pd.to_numeric(clean["weight_percent"], errors="coerce")
    clean = clean.dropna(subset=["weight_percent"])
    return clean


def _merge_sector_metrics(metrics: pd.DataFrame, sector_df: pd.DataFrame) -> pd.DataFrame:
    if sector_df.empty:
        metrics["sector_hhi_decimal"] = pd.NA
        metrics["sector_hhi_percent_points"] = pd.NA
        return metrics

    required = {"index_id", "index_name", "snapshot_date", "sector_weight_percent"}
    missing = required - set(sector_df.columns)
    if missing:
        raise ValueError(f"Missing required sector columns: {sorted(missing)}")

    sector_clean = sector_df.copy()
    sector_clean = sector_clean.dropna(subset=["index_id", "index_name", "snapshot_date", "sector_weight_percent"])
    sector_clean["sector_weight_percent"] = pd.to_numeric(sector_clean["sector_weight_percent"], errors="coerce")
    sector_clean = sector_clean.dropna(subset=["sector_weight_percent"])

    sector_metrics = sector_concentration_summary(
        sector_clean,
        sector_weight_col="sector_weight_percent",
        group_cols=["index_id", "index_name", "snapshot_date"],
        weights_are_percent=True,
    )

    return metrics.merge(
        sector_metrics,
        on=["index_id", "index_name", "snapshot_date"],
        how="left",
    )


def main() -> None:
    constituent_df = _read_csv_if_exists(CONSTITUENT_FILE)
    constituent_df = _validate_constituent_data(constituent_df)

    metrics = concentration_summary(
        constituent_df,
        weight_col="weight_percent",
        group_cols=["index_id", "index_name", "snapshot_date"],
        weights_are_percent=True,
    )

    if SECTOR_FILE.exists():
        sector_df = pd.read_csv(SECTOR_FILE)
        metrics = _merge_sector_metrics(metrics, sector_df)
    else:
        metrics["sector_hhi_decimal"] = pd.NA
        metrics["sector_hhi_percent_points"] = pd.NA

    if "coverage_type" in constituent_df.columns:
        coverage = (
            constituent_df.groupby(["index_id", "index_name", "snapshot_date"], dropna=False)["coverage_type"]
            .agg(lambda x: ",".join(sorted(set(x.dropna().astype(str)))))
            .reset_index()
        )
        metrics = metrics.merge(coverage, on=["index_id", "index_name", "snapshot_date"], how="left")

    # Basic data-quality flag: weights should be close to 100% for full-constituent datasets.
    metrics["data_quality_flag"] = "review"
    full_mask = metrics.get("coverage_type", pd.Series(index=metrics.index, dtype="object")).astype(str).str.contains("full", case=False, na=False)
    metrics.loc[full_mask & metrics["weight_sum_percent"].between(99.0, 101.0), "data_quality_flag"] = "ok"
    metrics.loc[full_mask & ~metrics["weight_sum_percent"].between(99.0, 101.0), "data_quality_flag"] = "weight_sum_check"

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    metrics.to_csv(OUTPUT_FILE, index=False)
    print(f"Wrote {len(metrics)} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
