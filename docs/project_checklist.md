# Project Checklist

## Priority 1: Foundation

- [x] Build Excel data collection template
- [x] Create `index_master.csv`
- [x] Create `constituent_weights.csv`
- [x] Create `sector_weights.csv`
- [x] Create `source_log.csv`
- [x] Add Python concentration-metrics module
- [x] Add runnable concentration-metrics script
- [x] Add risk-metrics module and runner script
- [x] Add data-quality validation script
- [x] Replace placeholder constituent weights with verified current index snapshots where available
- [x] Generate first HHI and top-weight summary table
- [x] Document BSE 500 exclusion for current snapshot

## Priority 2: Current Snapshot Data Assembly

- [x] Add current Nifty 50 snapshot
- [x] Add current Nifty Next 50 snapshot
- [x] Add current Nifty 100 snapshot
- [x] Add current Nifty 500 snapshot
- [x] Add current Nifty Bank snapshot
- [x] Add current Nifty IT snapshot
- [x] Add current Nifty FMCG snapshot
- [x] Add current Nifty Auto snapshot
- [x] Add current BSE Sensex snapshot
- [x] Add source URLs in the source log
- [x] Add index sample and coverage table

## Priority 3: Metric Computation

- [x] Implement HHI decimal and HHI percent-points calculations
- [x] Implement Top-3, Top-5, and Top-10 weights
- [x] Implement Effective N
- [x] Implement sector HHI functions
- [x] Implement Shannon entropy and Theil concentration
- [x] Add current-snapshot concentration summary output
- [x] Add current-snapshot chart
- [ ] Compare Excel output against Python output

## Priority 4: Risk Linkage

- [x] Add index return input template
- [x] Add index return source map
- [ ] Collect index price/value data
- [x] Add monthly return and drawdown calculation functions
- [x] Add annualized volatility and maximum drawdown functions
- [ ] Run risk metrics on populated index return data
- [ ] Build concentration-risk panel dataset
- [ ] Test relation between concentration and risk metrics

## Priority 5: Policy and Global Comparison

- [ ] Add global benchmark concentration metrics
- [ ] Add SEBI Significant Indices framework variables
- [ ] Compare AUM-threshold approach with concentration-risk ranking
- [ ] Identify potential framework gaps

## Priority 6: Paper Development

- [ ] Draft introduction
- [ ] Draft institutional background
- [ ] Draft literature review
- [ ] Draft methodology
- [ ] Insert empirical results
- [ ] Generate publication charts
- [ ] Draft working paper
