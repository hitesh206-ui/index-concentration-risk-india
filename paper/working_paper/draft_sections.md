# Draft Working Paper Sections

## Working Title

**Concentration Drift in Indian Equity Indices: Implications for Passive Investors and the SEBI Significant Indices Framework**

## 1. Introduction — Draft

The growth of passive investing has increased the importance of benchmark index design. Index funds, exchange-traded funds, structured products, and performance benchmarks all rely on index composition rules that appear diversified by constituent count but may still be economically concentrated in a small number of large stocks or sectors. This issue is particularly relevant in market-capitalisation-weighted indices, where rising prices and market capitalisation mechanically increase the weight of dominant firms.

India provides a useful setting to study this issue. Major Indian equity benchmarks such as the Nifty 50 and BSE Sensex are widely used by passive investors, institutions, and product issuers. Broader indices such as the Nifty 100 and Nifty 500 are often interpreted as more diversified, while sectoral indices such as Nifty Bank, Nifty IT, Nifty FMCG, and Nifty Auto are inherently more concentrated by design. However, the degree of concentration across these indices is not always transparent to retail investors.

This study examines concentration in Indian equity indices using constituent-weight and sector-weight data from public index factsheets and official index-weightage sources. The paper focuses on a current-snapshot analysis and distinguishes between full-constituent data, top-10-only constituent data, and sector-level data. This distinction is central to the research design because top-10-only concentration measures cannot be interpreted as full-index HHI measures.

The study contributes to the discussion on passive-investor risk, index governance, and benchmark transparency. It also relates to the SEBI Significant Indices framework by asking whether index significance should be evaluated only through product relevance and asset exposure, or whether concentration-based risk measures should also play a role.

## 2. Research Questions — Draft

This project is organised around four research questions:

1. How concentrated are major Indian equity indices when measured by top-constituent weights, HHI, effective number of stocks, and sector HHI?
2. Do broad market indices and sectoral indices differ materially in their concentration profiles?
3. How should researchers interpret concentration metrics when public factsheets provide only top-10 constituent weights rather than full constituent weights?
4. What are the implications of observed concentration for passive investors and index-governance frameworks?

## 3. Data and Sample Construction — Draft

The empirical sample currently consists of Indian equity indices for which current public constituent-weight or sector-weight information could be verified. The included indices are Nifty 50, Nifty Next 50, Nifty 100, Nifty 500, Nifty Bank, Nifty IT, Nifty FMCG, Nifty Auto, and BSE Sensex.

The NSE/Nifty index factsheets generally provide top-10 constituent weights and sector weights. For these indices, constituent-level concentration is reported as top-10 concentration rather than full-index constituent concentration. Nifty IT is treated as a full-constituent snapshot because the factsheet lists all 10 constituents. BSE Sensex is also treated as a full-constituent snapshot because official BSE scripwise weightage data were available.

BSE 500 is excluded from the current snapshot because a clean official current scripwise-weightage source comparable to the Sensex data was not verified at this stage. This exclusion is a data-quality decision rather than a claim about the relevance of the index.

## 4. Methodology — Draft

The study uses several concentration metrics. The first is the Herfindahl-Hirschman Index (HHI), calculated as the sum of squared constituent weights expressed in decimal form. The decimal HHI is also reported in percent-points by multiplying the decimal value by 10,000.

The effective number of stocks is calculated as the reciprocal of decimal HHI. A lower effective number indicates that the index behaves like a smaller equally weighted portfolio, even if the nominal number of constituents is larger.

The study also reports top-3, top-5, and top-10 constituent weights. These measures are especially useful when only top-10 constituent data are available from public factsheets. For sector-level analysis, the same HHI logic is applied to sector weights.

For entropy-based measurement, the project distinguishes between Shannon entropy and Theil concentration. Shannon entropy increases as weights become more evenly distributed, while Theil concentration increases as weight inequality rises.

## 5. Current Snapshot Findings — Placeholder

This section will present the current-snapshot concentration results after tables and charts are finalised.

Preliminary output tables are stored in:

```text
outputs/tables/current_snapshot_concentration_summary.csv
outputs/tables/index_sample_and_coverage.csv
```

Preliminary charts are stored in:

```text
outputs/charts/
```

## 6. Risk Linkage — Placeholder

The risk-linkage section will be completed after index-return data are populated and the risk-metrics pipeline is run. Planned risk metrics include periodic returns, rolling volatility, and maximum drawdown.

## 7. Limitations — Draft

The main limitation is data coverage. Several official public factsheets provide only the top-10 constituent weights rather than full constituent weights. Therefore, top-10 concentration metrics are not interpreted as full-index concentration metrics. The paper labels coverage type explicitly to avoid overclaiming.

A second limitation is that sectoral indices are single-sector exposures by construction. Their sector HHI is therefore mechanically high and should be interpreted as index-design concentration rather than accidental concentration drift.

A third limitation is that current-snapshot evidence does not by itself establish concentration drift over time. A historical extension will require comparable factsheets or historical weightage data across multiple dates.
