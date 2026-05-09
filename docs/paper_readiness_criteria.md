# Paper Readiness Criteria

## Purpose

This document defines when the project is ready to move from infrastructure and data construction to full paper writing.

## Current Position

The project is currently ready for a current-snapshot concentration analysis, but not yet ready for a full concentration-risk paper because index-return data are still pending.

## Minimum Criteria to Start the Full Paper

The full paper should be written only after the following are completed:

### 1. Current Snapshot Dataset Complete

- Current index concentration metrics are available.
- Coverage type is labelled for each index.
- Source URLs are recorded.
- BSE 500 exclusion is documented.

Status: complete for current snapshot.

### 2. Output Tables Generated

Required tables:

- Index sample and coverage table.
- Current snapshot concentration summary.
- Data quality report.
- Sector concentration summary.

Status: partly complete.

### 3. Charts Generated

Required charts:

- Top-10 constituent weight comparison.
- HHI comparison.
- Effective N comparison.
- Sector HHI comparison.

Status: partly complete.

### 4. Risk Data Added

Required file:

```text
data/processed/index_returns.csv
```

It should contain index-level data for included indices where available.

Status: pending.

### 5. Risk Metrics Generated

Required outputs:

```text
data/processed/index_returns_enriched.csv
data/processed/risk_metrics.csv
data/processed/concentration_risk_panel.csv
```

Status: pending.

### 6. Empirical Results Reviewed

Before writing conclusions, review:

- Which indices are most concentrated by Top-10 weight.
- Which indices are most concentrated by HHI.
- Which indices have the lowest Effective N.
- Whether concentration appears related to volatility or drawdown.
- Whether findings change depending on coverage type.

Status: pending.

## When to Write the Paper

### Start drafting now

The following sections can be drafted immediately:

- Introduction.
- Research questions.
- Institutional background.
- Data and sample construction.
- Methodology.
- Coverage limitations.

### Do not finalise yet

The following sections should wait until risk metrics and final tables are ready:

- Empirical results.
- Risk-linkage results.
- Policy implications.
- Conclusion.
- Abstract.

## Decision Rule

Write the full paper after:

```text
current snapshot tables + charts + risk metrics + concentration-risk panel are generated and reviewed
```

Until then, maintain draft sections but avoid final claims.
