# Writing Roadmap

## Current Writing Status

The paper should be treated as a structured working draft, not a final manuscript yet.

Draft sections already started:

- Introduction
- Research questions
- Data and sample construction
- Methodology
- Limitations

Sections that should wait:

- Abstract
- Empirical results
- Risk-linkage discussion
- Policy implications
- Conclusion

## Writing Sequence

### Phase 1: Draft Non-Result Sections

These can be written immediately:

1. Introduction
2. Institutional background
3. Literature review
4. Data and sample construction
5. Methodology
6. Coverage limitations

### Phase 2: Insert Current-Snapshot Results

Write after current-snapshot tables and charts are reviewed:

1. Current concentration comparison
2. Broad-index versus sectoral-index concentration
3. Full-constituent versus top-10-only interpretation
4. BSE 500 exclusion note

### Phase 3: Insert Risk Results

Write only after index-return data are populated and risk scripts are run:

1. Volatility comparison
2. Maximum drawdown comparison
3. Concentration-risk panel interpretation
4. Risk-linkage caveats

### Phase 4: Finalise Policy and Conclusion

Write after empirical results are stable:

1. SEBI framework implications
2. Passive-investor implications
3. Research limitations
4. Conclusion
5. Abstract

## Final Paper Trigger

Begin the full paper only after these files exist and are reviewed:

```text
outputs/tables/current_snapshot_concentration_summary.csv
outputs/tables/index_sample_and_coverage.csv
outputs/charts/current_snapshot_top10_weight.png
data/processed/risk_metrics.csv
data/processed/concentration_risk_panel.csv
```

## Current Recommendation

Start expanding the literature review and institutional background now. Do not finalise the abstract or conclusion until the risk-linkage outputs exist.
