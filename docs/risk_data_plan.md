# Risk Data Plan

## Objective

Build an index-level return dataset for the risk-linkage stage of the project.

## Preferred Source Hierarchy

1. Official NSE/BSE historical index data.
2. Public index-level data providers such as Yahoo Finance, used only where symbols are available and download output is verified.
3. Manual CSV upload from official index portals if automated download is unavailable.

## Current Yahoo Finance Symbol Coverage

The repository includes a Yahoo Finance symbol map for practical data collection.

Known or common symbols included:

- Nifty 50: `^NSEI`
- BSE Sensex: `^BSESN`
- Nifty Bank: `^NSEBANK`
- Nifty IT: `^CNXIT`

Other indices may require official NSE/BSE downloads or manual CSV input.

## Input File

Risk scripts expect:

```text
data/processed/index_returns.csv
```

Required columns:

```text
index_id,index_name,date,index_level,source_id,notes
```

## Pipeline

After populating `index_returns.csv`, run:

```bash
python scripts/run_risk_metrics.py
python scripts/build_concentration_risk_panel.py
```

## Outputs

```text
data/processed/index_returns_enriched.csv
data/processed/risk_metrics.csv
data/processed/concentration_risk_panel.csv
```

## Research Integrity Rule

Do not mix sources silently. Each index-return series must include a `source_id`, and source coverage limitations should be disclosed in the paper.
