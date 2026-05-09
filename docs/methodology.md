# Methodology

## Research Design

This project studies concentration drift in Indian equity indices and its implications for passive investors and index-governance regulation.

## Data Coverage Policy

All concentration metrics must be interpreted according to the available weight coverage.

### Full-Constituent Metrics

Use full-constituent metrics only when every index constituent weight is available for the snapshot.

Valid full-constituent metrics include:

- HHI decimal
- HHI percent-points
- Effective N
- Top-3, Top-5, and Top-10 weights
- Shannon entropy
- Theil concentration

### Top-10-Only Metrics

Use top-10-only metrics when the factsheet provides only the largest ten constituent weights.

Valid top-10-only metrics include:

- Top-3 weight
- Top-5 weight
- Top-10 weight
- partial top-10 HHI

Important limitation: top-10-only HHI is not the same as full index HHI. It should be labelled as partial concentration and not compared directly with full-constituent HHI.

### Sector-Level Metrics

Use sector-level metrics when the factsheet provides full sector distribution.

Valid sector-level metrics include:

- sector HHI decimal
- sector HHI percent-points
- top-sector weight

## Main Concentration Metrics

### Herfindahl-Hirschman Index

For an index with constituent weights `w_i` expressed as decimals:

```text
HHI_decimal = sum(w_i^2)
```

The percent-points version is:

```text
HHI_percent_points = HHI_decimal * 10000
```

Higher HHI indicates greater concentration.

### Effective Number of Stocks

```text
Effective N = 1 / HHI_decimal
```

This estimates the number of equally weighted constituents that would generate the same concentration level.

### Top-N Weights

```text
Top-N Weight = sum of the largest N constituent weights
```

Planned metrics:

- Top-3 weight
- Top-5 weight
- Top-10 weight

### Sector HHI

Sector HHI applies the same HHI formula to sector-level index weights.

### Shannon Entropy and Theil Concentration

Shannon entropy is calculated as:

```text
Shannon Entropy = -sum(w_i * ln(w_i))
```

Theil concentration is calculated as:

```text
Theil Concentration = ln(N) - Shannon Entropy
```

Shannon entropy increases with diversification. Theil concentration increases with concentration.

## Risk Metrics

The project will examine whether concentration is associated with:

- index volatility
- maximum drawdown
- tracking-error proxy
- sector concentration risk

## Planned Sample

### Indian Indices

- Nifty 50
- Nifty Next 50
- Nifty 100
- Nifty 500
- BSE Sensex
- BSE 500
- Nifty Bank
- Nifty IT
- Nifty FMCG
- Nifty Auto

### Global Benchmarks

- S&P 500
- FTSE 100
- Nikkei 225
- MSCI Emerging Markets

## Planned Period

January 2015 to April 2026, subject to availability of historical factsheets.

If monthly historical factsheets are incomplete, the paper will use the most granular verified frequency available and clearly disclose the limitation.

## SEBI Framework Analysis

The study will evaluate whether SEBI's Significant Indices framework captures indices with high concentration risk or whether important gaps remain when risk is measured by concentration rather than AUM alone.
