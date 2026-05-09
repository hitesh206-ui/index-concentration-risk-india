"""Generate sector concentration summary from sector_weights.csv.

Run from repository root:
    python scripts/generate_sector_summary.py

Input:
    data/processed/sector_weights.csv

Output:
    outputs/tables/sector_concentration_summary.csv
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.concentration_metrics import hhi_decimal, hhi_percent_points


ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "processed" / "sector_weights.csv"
OUTPUT_FILE = ROOT / "outputs" / "tables" / "sector_concentration_summary.csv"


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Missing input file: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)
    required = {"index_id", "index_name", "snapshot_date", "sector", "sector_weight_percent"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df["sector_weight_percent"] = pd.to_numeric(df["sector_weight_percent"], errors="coerce")
    df = df.dropna(subset=["sector_weight_percent"])

    rows = []
    for keys, group in df.groupby(["index_id", "index_name", "snapshot_date"], dropna=False):
        index_id, index_name, snapshot_date = keys
        sorted_group = group.sort_values("sector_weight_percent", ascending=False)
        top_sector = sorted_group.iloc[0]
        weights = sorted_group["sector_weight_percent"].tolist()
        rows.append(
            {
                "index_id": index_id,
                "index_name": index_name,
                "snapshot_date": snapshot_date,
                "sector_count": int(sorted_group.shape[0]),
                "top_sector": top_sector["sector"],
                "top_sector_weight_percent": float(top_sector["sector_weight_percent"]),
                "sector_hhi_decimal": hhi_decimal(weights, weights_are_percent=True),
                "sector_hhi_percent_points": hhi_percent_points(weights, weights_are_percent=True),
            }
        )

    out = pd.DataFrame(rows)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUTPUT_FILE, index=False)
    print(f"Wrote {len(out)} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
