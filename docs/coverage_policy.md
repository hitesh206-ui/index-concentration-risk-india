# Coverage Policy: Full Constituents vs Top-10 vs Sector Data

## Why This Matters

Index concentration metrics depend heavily on the coverage of the underlying weight data. A full constituent dataset and a top-10-only dataset cannot be interpreted the same way.

## Coverage Types

### 1. `full_constituents`

Use this label only when the dataset includes every constituent weight for the index snapshot.

Examples:

- all 50 weights for Nifty 50
- all 30 weights for Sensex
- all 500 weights for Nifty 500 or BSE 500

Metrics that are valid under full coverage:

- HHI
- Effective N
- Top-3 weight
- Top-5 weight
- Top-10 weight
- Shannon entropy
- Theil concentration

### 2. `top10_only`

Use this label when the source provides only the top-10 constituent weights.

Metrics that are valid under top-10-only coverage:

- Top-3 weight
- Top-5 weight
- Top-10 weight
- partial HHI based only on top-10 weights

Important limitation:

Top-10-only HHI is not the full index HHI. It is a partial or lower-bound concentration measure and should not be compared directly with full-constituent HHI.

### 3. `sector_only`

Use this label when the source provides sector weights but not full constituent weights.

Metrics that are valid under sector-only coverage:

- sector HHI
- top-sector concentration
- sector entropy if implemented later

## Current Nifty 50 Treatment

The official Nifty 50 factsheet snapshot currently used in this project provides:

- top-10 constituent weights
- full sector weights

Therefore, the current Nifty 50 dataset is treated as:

```text
constituent coverage: top10_only
sector coverage: full sector weights
```

The paper must not describe this as full constituent concentration until all 50 constituent weights are obtained from a reliable source.

## Research Reporting Rule

Every table and chart must state whether it is based on:

- full constituent data
- top-10-only data
- sector-level data

This prevents overclaiming and protects the credibility of the research.
