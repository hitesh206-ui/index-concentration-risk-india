"""Create empty CSV templates for the index concentration project."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


TEMPLATES = {
    "index_master.csv": [
        "index_id",
        "index_name",
        "index_provider",
        "index_type",
        "country",
        "currency",
        "constituent_count_target",
        "notes",
    ],
    "constituent_weights.csv": [
        "index_id",
        "index_name",
        "snapshot_date",
        "constituent_name",
        "ticker",
        "sector",
        "weight",
        "coverage_type",
        "source_id",
    ],
    "sector_weights.csv": [
        "index_id",
        "index_name",
        "snapshot_date",
        "sector",
        "sector_weight",
        "source_id",
    ],
    "concentration_metrics.csv": [
        "index_id",
        "index_name",
        "snapshot_date",
        "constituent_count",
        "weight_sum_percent",
        "hhi",
        "effective_n",
        "top3_weight",
        "top5_weight",
        "top10_weight",
        "theil_entropy",
        "sector_hhi",
        "coverage_type",
    ],
    "source_log.csv": [
        "source_id",
        "index_name",
        "snapshot_date",
        "source_type",
        "source_url",
        "notes",
    ],
}


def create_templates(output_dir: str | Path = "data/processed") -> None:
    """Create empty CSV template files if they do not already exist."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for filename, columns in TEMPLATES.items():
        path = output_path / filename
        if not path.exists():
            pd.DataFrame(columns=columns).to_csv(path, index=False)


if __name__ == "__main__":
    create_templates()
