"""Standardize manually downloaded index-level CSV files.

Purpose
-------
Some indices may not have reliable Yahoo Finance symbols. For those cases,
download historical index data from official NSE/BSE portals and place the
cleaned CSVs in:

    data/raw/index_returns/

Expected raw columns can vary, but the script looks for common names such as:
    Date, date, Index Date
    Close, close, Closing Value, close_price, index_level

Output:
    data/processed/index_returns_manual_standardized.csv

After review, this file can be appended to:
    data/processed/index_returns.csv
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw" / "index_returns"
OUTPUT_FILE = ROOT / "data" / "processed" / "index_returns_manual_standardized.csv"

DATE_CANDIDATES = ["Date", "date", "Index Date", "INDEX_DATE", "HistoricalDate"]
LEVEL_CANDIDATES = ["Close", "close", "Closing Value", "close_price", "index_level", "CLOSE"]


def _find_column(columns: list[str], candidates: list[str]) -> str | None:
    normalized = {col.strip().lower(): col for col in columns}
    for candidate in candidates:
        key = candidate.strip().lower()
        if key in normalized:
            return normalized[key]
    return None


def standardize_file(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    date_col = _find_column(list(df.columns), DATE_CANDIDATES)
    level_col = _find_column(list(df.columns), LEVEL_CANDIDATES)

    if date_col is None or level_col is None:
        raise ValueError(f"Could not identify date/index-level columns in {path.name}")

    # Filename convention: INDEXID__Index Name.csv, e.g. NIFTY100__Nifty 100.csv
    stem = path.stem
    if "__" in stem:
        index_id, index_name = stem.split("__", 1)
        index_name = index_name.replace("_", " ")
    else:
        index_id = stem.upper().replace(" ", "_")
        index_name = stem.replace("_", " ")

    out = pd.DataFrame(
        {
            "index_id": index_id,
            "index_name": index_name,
            "date": pd.to_datetime(df[date_col], errors="coerce"),
            "index_level": pd.to_numeric(df[level_col], errors="coerce"),
            "source_id": "MANUAL_" + index_id,
            "notes": "Standardized from manual official/source CSV: " + path.name,
        }
    )
    out = out.dropna(subset=["date", "index_level"])
    out["date"] = out["date"].dt.date
    return out


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(RAW_DIR.glob("*.csv"))
    if not files:
        raise FileNotFoundError(
            f"No CSV files found in {RAW_DIR}. Add official/manual index return CSVs first."
        )

    frames = []
    for file in files:
        frames.append(standardize_file(file))

    result = pd.concat(frames, ignore_index=True)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUTPUT_FILE, index=False)
    print(f"Wrote {len(result)} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
