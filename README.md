# Index Concentration Risk in India

This repository supports the research project:

**Concentration Drift in Indian Equity Indices: Implications for Passive Investors and the SEBI Significant Indices Framework**

## Research Objective

This project examines whether concentration in major Indian equity indices has increased over time, whether concentration is related to passive-investor risk, and whether the SEBI Significant Indices framework captures the indices most exposed to concentration risk.

## Core Research Questions

1. Has concentration in major Indian equity indices increased materially over the past decade?
2. How does Indian index concentration compare with global benchmarks such as the S&P 500, FTSE 100, Nikkei 225, and MSCI Emerging Markets?
3. Does index concentration correlate with volatility, drawdown depth, and tracking-error risk?
4. Does the SEBI Significant Indices framework capture the indices with the highest concentration risk?

## Planned Indices

### Broad Indian Indices

- Nifty 50
- Nifty Next 50
- Nifty 100
- Nifty 500
- BSE Sensex
- BSE 500

### Sectoral Indian Indices

- Nifty Bank
- Nifty IT
- Nifty FMCG
- Nifty Auto

### Global Benchmarks

- S&P 500
- FTSE 100
- Nikkei 225
- MSCI Emerging Markets

## Planned Metrics

- Herfindahl-Hirschman Index (HHI)
- Top-3 constituent weight
- Top-5 constituent weight
- Top-10 constituent weight
- Effective number of stocks (`1 / HHI`)
- Sector HHI
- Theil entropy
- volatility
- maximum drawdown
- tracking-error proxy

## Data Sources

The project is designed to use public internet data:

- NSE/Nifty index factsheets
- BSE index factsheets
- NSE/BSE index-value data
- Yahoo Finance or equivalent public market data for index returns
- Wayback Machine snapshots where historical factsheets are not directly available
- Public factsheets for selected global benchmarks

## Repository Structure

```text
├── data/
│   ├── raw/
│   ├── processed/
│   └── documentation/
├── notebooks/
├── src/
├── outputs/
│   ├── charts/
│   ├── tables/
│   └── excel/
├── paper/
│   ├── draft/
│   └── ssrn_submission/
└── docs/
```

## Current Status

The project is in the foundation-building stage. The first milestone is to build a working Excel/Python pipeline using current Nifty 50 constituent weights before expanding to historical monthly data.

## Disclaimer

This repository is for academic and educational research purposes only. It does not provide investment advice. Third-party factsheets and source documents should be referenced through links rather than redistributed if licensing is unclear.
