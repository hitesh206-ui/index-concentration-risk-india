"""Create index level dataset from Yahoo Finance symbols.

Run from repository root:
    python scripts/get_index_returns_yfinance.py

Output:
    data/processed/index_returns.csv
    outputs/tables/yfinance_download_report.csv

Official NSE/BSE historical files remain preferred where available. This script
is a practical fallback for indices with public Yahoo Finance symbols.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed"
REPORT_DIR = ROOT / "outputs" / "tables"
MAP_FILE = ROOT / "data" / "documentation" / "yfinance_symbol_map.csv"
OUTPUT_FILE = DATA_DIR / "index_returns.csv"
REPORT_FILE = REPORT_DIR / "yfinance_download_report.csv"
START_DATE = "2021-01-01"


def read_symbol_map() -> pd.DataFrame:
    table = pd.read_csv(MAP_FILE)
    table = table.dropna(subset=["yfinance_symbol"])
    table = table[table["yfinance_symbol"].astype(str).str.strip() != ""]
    return table


def fetch_symbol(index_id: str, index_name: str, symbol: str) -> tuple[pd.DataFrame, dict]:
    report = {
        "index_id": index_id,
        "index_name": index_name,
        "symbol": symbol,
        "status": "not_started",
        "row_count": 0,
        "start_date": "",
        "end_date": "",
        "message": "",
    }
    try:
        raw = yf.download(symbol, start=START_DATE, progress=False, auto_adjust=False, threads=False)
    except Exception as exc:
        report["status"] = "error"
        report["message"] = str(exc)
        return pd.DataFrame(), report

    if raw.empty:
        report["status"] = "empty"
        report["message"] = "No rows returned"
        return pd.DataFrame(), report

    if isinstance(raw.columns, pd.MultiIndex):
        close_cols = [col for col in raw.columns if col[0] in {"Adj Close", "Close"}]
        series = raw[close_cols[0]] if close_cols else raw.iloc[:, 0]
    else:
        series = raw["Adj Close"] if "Adj Close" in raw.columns else raw["Close"]

    out = pd.DataFrame(
        {
            "index_id": index_id,
            "index_name": index_name,
            "date": series.index.date,
            "index_level": series.to_numpy(),
            "source_id": "YFINANCE_" + symbol.replace("^", "").replace(".", "_"),
            "notes": "Yahoo Finance symbol " + symbol,
        }
    )
    out = out.dropna(subset=["index_level"])
    report["status"] = "ok" if not out.empty else "empty_after_cleaning"
    report["row_count"] = int(len(out))
    if not out.empty:
        report["start_date"] = str(out["date"].min())
        report["end_date"] = str(out["date"].max())
    return out, report


def main() -> None:
    frames = []
    reports = []
    for _, row in read_symbol_map().iterrows():
        symbol = str(row["yfinance_symbol"]).strip()
        data, report = fetch_symbol(str(row["index_id"]), str(row["index_name"]), symbol)
        reports.append(report)
        if not data.empty:
            frames.append(data)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(reports).to_csv(REPORT_FILE, index=False)

    if not frames:
        # Keep an empty template so downstream failure is clear but file exists.
        pd.DataFrame(columns=["index_id", "index_name", "date", "index_level", "source_id", "notes"]).to_csv(OUTPUT_FILE, index=False)
        raise RuntimeError("No index level data returned. See outputs/tables/yfinance_download_report.csv")

    result = pd.concat(frames, ignore_index=True)
    result.to_csv(OUTPUT_FILE, index=False)
    print(f"Wrote {len(result)} rows to {OUTPUT_FILE}")
    print(f"Wrote download report to {REPORT_FILE}")


if __name__ == "__main__":
    main()
