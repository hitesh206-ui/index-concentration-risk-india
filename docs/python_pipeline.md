# Python Pipeline

## Purpose

The Python pipeline calculates concentration metrics from the processed CSV data files.

## Input Files

Place cleaned input files here:

```text
data/processed/constituent_weights.csv
data/processed/sector_weights.csv
```

## Required Constituent Columns

```text
index_id
index_name
snapshot_date
constituent_name
weight_percent
```

Optional but recommended:

```text
constituent_rank
ticker
sector
coverage_type
source_id
```

## Required Sector Columns

```text
index_id
index_name
snapshot_date
sector
sector_weight_percent
```

## Run Command

From the repository root:

```bash
python scripts/run_concentration_metrics.py
```

## Output File

The script writes:

```text
data/processed/concentration_metrics.csv
```

## Metrics Generated

- constituent count
- weight sum percent
- HHI decimal
- HHI percent-points
- effective number of stocks
- Top-3 weight
- Top-5 weight
- Top-10 weight
- Shannon entropy
- Theil concentration
- sector HHI decimal
- sector HHI percent-points
- data quality flag

## Important Data Rule

Weights must be entered in percentage form, not decimal form.

Correct:

```text
13.63
```

Incorrect:

```text
0.1363
```
