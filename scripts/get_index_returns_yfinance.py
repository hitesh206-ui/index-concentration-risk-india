"""Create index level dataset from Yahoo Finance symbols.

Run from repository root:
    python scripts/get_index_returns_yfinance.py

Output:
    data/processed/index_returns.csv
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed"
MAP_FILE = ROOT / "data" / "documentation" / "yfinance_symbol_map.csv"
OUTPUT_FILE = DATA_DIR / "index_returns.csv"
START_DATE = "2021-01-01"


def read_symbol_map() -> pd.DataFrame:
    table = pd.read_csv(MAP_FILE)
    table = table.dropna(subset=["yfinance_symbol"])
    table = table[table["yfinance_symbol"].astype(str).str.strip() != ""]
    return table


def fetch_symbol(index_id: str, index_name: str, symbol: str) -> pd.DataFrame:
    raw = yf.download(symbol, start=START_DATE, progress=False, auto_adjust=False)
    if raw.empty:
        return pd.DataFrame()

    if isinstance(raw.columns, pd.MultiIndex):
        close_cols = [col for col in raw.columns if col[0] in {"Adj Close", "Close"}]
        series = raw[close_cols[0]] if close_cols else raw.iloc[:, 0]
    else:
        series = raw["Adj Close"] if "Adj Close" in raw.columns else raw["Close"]

    return pd.DataFrame(
        {
            "index_id": index_id,
            "index_name": index_name,
            "date": series.index.date,
            "index_level": series.to_numpy(),
            "source_id": "YFINANCE_" + symbol.replace("^", "").replace(".", "_"),
            "notes": "Yahoo Finance symbol " + symbol,
        }
    )


def main() -> None:
    frames = []
    for _, row in read_symbol_map().iterrows():
        symbol = str(row["yfinance_symbol"]).strip()
        data = fetch_symbol(str(row["index_id"]), str(row["index_name"]), symbol)
        if not data.empty:
            frames.append(data)

    if not frames:
        raise RuntimeError("No index level data returned. Check symbols and connection.")

    result = pd.concat(frames, ignore_index=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUTPUT_FILE, index=False)
    print(f"Wrote {len(result)} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
