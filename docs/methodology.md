# Methodology

## Research Design

This project studies concentration drift in Indian equity indices and its implications for passive investors and index-governance regulation.

## Main Concentration Metrics

### Herfindahl-Hirschman Index

For an index with constituent weights `w_i` expressed as decimals:

```text
HHI = sum(w_i^2)
```

Higher HHI indicates greater concentration.

### Effective Number of Stocks

```text
Effective N = 1 / HHI
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

### Theil Entropy

Theil entropy captures inequality across constituent weights.

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
