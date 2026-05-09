# Project Checklist

## Priority 1: Foundation

- [x] Build Excel data collection template
- [x] Create `index_master.csv`
- [x] Create `constituent_weights.csv`
- [x] Create `sector_weights.csv`
- [x] Create `source_log.csv`
- [x] Add Python concentration-metrics module
- [x] Add runnable concentration-metrics script
- [ ] Replace placeholder constituent weights with verified current Nifty 50 data
- [ ] Test concentration metrics on verified current Nifty 50 weights
- [ ] Generate first HHI and top-weight summary table

## Priority 2: Historical Data Assembly

- [ ] Collect current factsheets for all planned Indian indices
- [ ] Collect historical factsheet snapshots for Nifty 50, Sensex, and Nifty 500
- [ ] Expand to Nifty Next 50, Nifty 100, BSE 500, and sectoral indices
- [ ] Mark each observation as monthly, quarterly, annual, or current snapshot
- [ ] Record all source URLs in the source log

## Priority 3: Metric Computation

- [x] Implement HHI decimal and HHI percent-points calculations
- [x] Implement Top-3, Top-5, and Top-10 weights
- [x] Implement Effective N
- [x] Implement sector HHI functions
- [x] Implement Shannon entropy and Theil concentration
- [ ] Validate weight sums on verified data
- [ ] Compare Excel output against Python output

## Priority 4: Risk Linkage

- [ ] Collect index price/value data
- [ ] Compute monthly returns
- [ ] Compute annualized volatility
- [ ] Compute maximum drawdown
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
