# Excel Template Validation Notes

## Template Version

Current validated workbook version: `v1.1 - formula-fixed`

## Fixes Applied

### 1. Top-N Weight Formulas

The original workbook used dynamic-array formulas for Top-3, Top-5, and Top-10 weights. These were replaced with more compatible rank-based formulas.

### 2. Index Return Formulas

Monthly return and drawdown formulas were corrected so each row references the appropriate current and prior row.

Correct monthly return logic:

```text
current_index_level / prior_index_level - 1
```

Correct drawdown logic:

```text
current_index_level / running_max_index_level - 1
```

### 3. HHI Scale

HHI is now calculated in percent-points squared:

```text
HHI = sum(weight_percent^2)
```

Effective number of stocks is calculated as:

```text
Effective N = 10000 / HHI
```

### 4. Entropy Metric

An entropy-style concentration metric has been added to the `Concentration_Metrics` sheet.

### 5. Sample Data

The sample Nifty 50 rows are placeholders for testing workbook structure and formulas. They must be replaced or verified against actual factsheet data before analysis.

### 6. Validation Sheet

A `Template_Validation` sheet was added to document fixes and formula-check status.

## Final Check

The workbook was scanned for common spreadsheet formula errors. No formula-error matches were found in the final scan.
