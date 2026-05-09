"""Validate processed data files for the index concentration project.

Usage from repository root:

    python scripts/validate_data_quality.py

Outputs:
    outputs/tables/data_quality_report.csv
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed"
OUTPUT_DIR = ROOT / "outputs" / "tables"
REPORT_FILE = OUTPUT_DIR / "data_quality_report.csv"


def _add_check(rows: list[dict], check_name: str, status: str, detail: str) -> None:
    rows.append({"check_name": check_name, "status": status, "detail": detail})


def validate_constituent_weights(rows: list[dict]) -> None:
    path = DATA_DIR / "constituent_weights.csv"
    if not path.exists():
        _add_check(rows, "constituent_weights_exists", "fail", f"Missing {path}")
        return

    df = pd.read_csv(path)
    required = {"index_id", "index_name", "snapshot_date", "constituent_name", "weight_percent"}
    missing = required - set(df.columns)
    if missing:
        _add_check(rows, "constituent_required_columns", "fail", f"Missing {sorted(missing)}")
        return
    _add_check(rows, "constituent_required_columns", "pass", "All required columns present")

    df["weight_percent"] = pd.to_numeric(df["weight_percent"], errors="coerce")
    bad_weights = df["weight_percent"].isna().sum()
    _add_check(rows, "constituent_numeric_weights", "pass" if bad_weights == 0 else "warn", f"Non-numeric weights: {bad_weights}")

    missing_dates = df["snapshot_date"].isna().sum() + (df["snapshot_date"].astype(str).str.strip() == "").sum()
    _add_check(rows, "constituent_snapshot_dates", "pass" if missing_dates == 0 else "warn", f"Missing snapshot dates: {missing_dates}")

    if "coverage_type" in df.columns:
        full = df[df["coverage_type"].astype(str).str.contains("full", case=False, na=False)].copy()
        if not full.empty:
            sums = full.groupby(["index_id", "snapshot_date"], dropna=False)["weight_percent"].sum()
            failed = sums[(sums < 99.0) | (sums > 101.0)]
            _add_check(
                rows,
                "full_weight_sum_99_101",
                "pass" if failed.empty else "warn",
                f"Full-coverage snapshots outside 99-101 percent: {len(failed)}",
            )
        else:
            _add_check(rows, "full_weight_sum_99_101", "warn", "No full-coverage snapshots found")

    decimal_like = (df["weight_percent"].dropna() < 1).mean() if df["weight_percent"].dropna().shape[0] else 0
    if decimal_like > 0.8:
        _add_check(rows, "weight_scale_check", "warn", "Most weights are below 1; confirm weights are percentages, not decimals")
    else:
        _add_check(rows, "weight_scale_check", "pass", "Weights appear to be in percentage units")


def validate_index_returns(rows: list[dict]) -> None:
    path = DATA_DIR / "index_returns.csv"
    if not path.exists():
        _add_check(rows, "index_returns_exists", "warn", f"Missing {path}; needed for risk-linkage stage")
        return

    df = pd.read_csv(path)
    required = {"index_id", "index_name", "date", "index_level"}
    missing = required - set(df.columns)
    if missing:
        _add_check(rows, "index_returns_required_columns", "fail", f"Missing {sorted(missing)}")
        return
    _add_check(rows, "index_returns_required_columns", "pass", "All required columns present")

    df["index_level"] = pd.to_numeric(df["index_level"], errors="coerce")
    bad_levels = df["index_level"].isna().sum()
    _add_check(rows, "index_levels_numeric", "pass" if bad_levels == 0 else "warn", f"Non-numeric index levels: {bad_levels}")


def main() -> None:
    rows: list[dict] = []
    validate_constituent_weights(rows)
    validate_index_returns(rows)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report = pd.DataFrame(rows)
    report.to_csv(REPORT_FILE, index=False)
    print(report.to_string(index=False))
    print(f"Wrote data quality report to {REPORT_FILE}")


if __name__ == "__main__":
    main()
