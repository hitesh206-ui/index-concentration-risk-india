# Data Dictionary

## `index_master.csv`

| Variable | Description |
|---|---|
| `index_id` | Short unique identifier for each index. |
| `index_name` | Full index name. |
| `provider` | Index provider, such as NSE Indices or BSE. |
| `country` | Country or market. |
| `index_type` | Broad, sectoral, thematic, or global benchmark. |
| `category` | Large-cap, multi-cap, sector, etc. |
| `currency` | Index currency. |
| `target_constituent_count` | Intended number of constituents in the index. |
| `start_date` | Index start or base date if available. |
| `included_in_study` | Whether the index is included in the research sample. |
| `notes` | Additional comments. |

## `constituent_weights.csv`

| Variable | Description |
|---|---|
| `obs_id` | Observation identifier. |
| `index_id` | Index identifier. |
| `index_name` | Full index name. |
| `snapshot_date` | Factsheet or weight snapshot date. |
| `constituent_rank` | Rank by index weight. |
| `constituent_name` | Company or constituent name. |
| `ticker` | Exchange ticker if available. |
| `sector` | Sector classification. |
| `weight_percent` | Constituent weight in percent units. Example: 13.63 means 13.63 percent. |
| `coverage_type` | `full_constituents`, `top10_only`, or other documented coverage. |
| `source_id` | Links observation to the source log. |
| `notes` | Additional comments. |

## `sector_weights.csv`

| Variable | Description |
|---|---|
| `obs_id` | Observation identifier. |
| `index_id` | Index identifier. |
| `index_name` | Full index name. |
| `snapshot_date` | Factsheet or sector-weight snapshot date. |
| `sector` | Sector name. |
| `sector_weight_percent` | Sector weight in percent units. |
| `source_id` | Links observation to the source log. |
| `notes` | Additional comments. |

## `concentration_metrics.csv`

| Variable | Description |
|---|---|
| `index_id` | Index identifier. |
| `index_name` | Full index name. |
| `snapshot_date` | Weight snapshot date. |
| `constituent_count` | Number of constituent weights available for the snapshot. |
| `weight_sum_percent` | Sum of available constituent weights. |
| `hhi_decimal` | Herfindahl-Hirschman Index in decimal scale, equal to sum of squared decimal weights. |
| `hhi_percent_points` | HHI in percent-points squared, equal to `hhi_decimal * 10000`. |
| `effective_n` | Effective number of equally weighted stocks, equal to `1 / hhi_decimal`. |
| `top3_weight_percent` | Combined weight of the three largest constituents. |
| `top5_weight_percent` | Combined weight of the five largest constituents. |
| `top10_weight_percent` | Combined weight of the ten largest constituents. |
| `shannon_entropy` | Diversification-oriented entropy measure. Higher values imply more even weights. |
| `theil_concentration` | Concentration-oriented inequality measure. Higher values imply more concentration. |
| `sector_hhi_decimal` | Sector-level HHI in decimal scale. |
| `sector_hhi_percent_points` | Sector-level HHI in percent-points squared. |
| `coverage_type` | Indicates whether metrics are based on full constituents or partial top-weight data. |
| `data_quality_flag` | Data-quality status assigned by the pipeline. |

## `index_returns.csv`

| Variable | Description |
|---|---|
| `index_id` | Index identifier. |
| `index_name` | Full index name. |
| `date` | Date of index level observation. |
| `index_level` | Closing index level. |
| `source_id` | Links observation to source log if applicable. |

## `risk_metrics.csv`

| Variable | Description |
|---|---|
| `index_id` | Index identifier. |
| `index_name` | Full index name. |
| `observation_count` | Number of index-level observations. |
| `start_date` | First date in the return sample. |
| `end_date` | Last date in the return sample. |
| `mean_periodic_return` | Average periodic return. |
| `annualized_volatility` | Annualized volatility based on periodic returns. |
| `maximum_drawdown` | Maximum drawdown over the sample period. |
