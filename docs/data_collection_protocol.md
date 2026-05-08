# Data Collection Protocol

## Objective

Build a reproducible dataset of index constituent weights, sector weights, and index return data for Indian and selected global equity indices.

## Primary Data Sources

### Indian Indices

- NSE/Nifty index factsheets
- NSE/Nifty historical index data
- BSE/Sensex factsheets
- BSE index data
- Wayback Machine snapshots for historical factsheets

### Global Benchmarks

- S&P 500 public factsheets or constituent-weight summaries
- FTSE 100 public factsheets or constituent-weight summaries
- Nikkei 225 public factsheets or constituent-weight summaries
- MSCI Emerging Markets public factsheets or constituent-weight summaries

## Target Data Frequency

Preferred frequency: monthly.

Fallback frequency: quarterly or annual snapshots if monthly historical factsheets are incomplete.

## Processed Data Files

Recommended processed files:

```text
data/processed/index_master.csv
data/processed/constituent_weights.csv
data/processed/sector_weights.csv
data/processed/concentration_metrics.csv
data/processed/index_returns.csv
data/processed/global_benchmarks.csv
```

## Source Log

Every data point should be traceable to a source URL.

Use:

```text
data/documentation/source_log.csv
```

Minimum fields:

- source_id
- index_name
- snapshot_date
- source_type
- source_url
- notes

## Data Quality Rules

1. Constituent weights should sum close to 100 percent.
2. If a source reports only top-10 constituents, mark `coverage_type = top10_only`.
3. If full constituent weights are available, mark `coverage_type = full_constituents`.
4. Do not mix full-weight and top-10-only HHI without labelling the coverage difference.
5. Use decimal weights in Python calculations, not percentage units.
6. Preserve original factsheet date or snapshot date.
7. Do not fill missing historical months unless the interpolation rule is explicitly documented.

## Minimum Viable Dataset

Start with current index factsheets for Nifty 50, Nifty Next 50, Nifty 100, Nifty 500, Sensex, and BSE 500. Then expand to historical snapshots.
