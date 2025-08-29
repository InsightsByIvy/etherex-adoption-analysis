# Etherex Adoption Analysis
A data-driven analysis of Etherex on Linea, focusing on genuine user adoption, liquidity efficiency, and protocol incentives using Dune Analytics.


## Table of Contents

1. [Introduction](#introduction)
   - Project Overview
   - Objective of the Dashboard
   - Why Etherex & Linea

2. [Dashboard Overview](#dashboard-overview)
   - Summary of the 8 Charts
   - Key Metrics & KPIs
   - Data Sources (Dune, CoinGecko, DefiLlama, etc.)

3. [Methodology](#methodology)
   - Data Collection Process
   - SQL Queries & API Scripts
   - Chart Explanation
   - Filtering Bots vs Genuine Users
   - Assumptions & Definitions

4. [Insights & Analysis](#insights--analysis)
   - Adoption Quality (Regular vs Genuine Users)
   - Liquidity Efficiency & Capital Utilization
   - Fee Yield & Incentive Alignment
   - Slippage & Trading Efficiency
   - MEV / Sandwich Exposure Analysis
  
5. [Target Audience & Use Cases](#target-audience--use-cases)
   - Protocol Team: Understand adoption quality, liquidity health, and tokenomics efficiency
   - Advisors / Analysts: Evaluate market traction, growth potential, and risk exposure
   - Subscribers / Community: Transparency into genuine user engagement and protocol performance

5. [Resources & References](#resources--references)
   - Articles, Reports, and Whitepapers
   - Dune Queries & Documentation Links

6. [Repo Structure](#repo-structure)
   - Description of Folders and Files
   - How to Reproduce / Run the Scripts

7. [Conclusion](#conclusion)
   - Key Takeaways
   - Limitations & Next Steps
  
## 1. Introduction
### Project Overview

"Linea’s vibrant new DEX". Linea is an emerging L2 ecosystem with rapid TVL growth. Early activity in Etherex (DEX) and Aave (lending) shows increasing user adoption and capital inflows. 

Source: https://x.com/etherexfi/status/1947132627737309399

## 2. Dashboard Overview
This dashboard provides a structured view of Etherex performance within the Linea ecosystem. The charts are grouped by stakeholder audience: Protocol Teams, Advisors/Investors, and Subscribers/Users.
By structuring the data this way, the dashboard moves beyond raw numbers to deliver actionable insights tailored to each audience.

Data is sourced from Dune Analytics and is presented with a balance of technical accuracy and strategic interpretation.

#### 1. Protocol Teams  
**Focus:** Internal Etherex health, incentive effectiveness, and liquidity engagement.  
These metrics help protocol maintainers gauge how incentives perform and where improvements may be needed.  

**Key Charts**
- **Daily REX Staking Behavior**  
  *Monitors adoption of staking and conversion to xREX.*  
- **Emission Effectiveness (Weekly Staking vs. DEX Activity)**  
  - Tests whether staking incentives (xREX rewards) successfully increase liquidity on Etherex.  
  - Identifies weeks where higher staking aligns with higher DEX trading activity.  
  - Helps answer: *Are incentives attracting genuine users and volume to Etherex?*  

---

#### 2. Advisors / Investors  
**Focus:** Economic and growth signals to evaluate Etherex’s long-term performance and viability.  

**Key Charts**
- **xREX Fee Earnings Potential**  
  *Compares cumulative staking to fee/revenue generation for stakers.*  
  - Insight: Demonstrates protocol value capture, critical for assessing Etherex sustainability.  
- **Trading Pair Concentration**  
  *Shows whether liquidity is diversified or concentrated in a few pairs.*  
  - Insight: Reveals dependency risks and scaling opportunities across Etherex markets.  

---

#### 3. User Behavior & Engagement  
**Focus:** Community health and adoption quality on Etherex.  

**Key Charts**
- **Real vs. Bot Users**  
  *Filters out non-genuine wallets to measure authentic participation.*  
  - Insight: Distinguishes sustainable adoption from inflated metrics.  
- **Post-Launch Activity Sustainability**  
  *Analyzes whether users remain engaged after initial launch momentum.*  

---

#### 4. Ecosystem & Macro-Level Indicators  
**Focus:** Etherex’s role in the wider Linea ecosystem and cross-chain dynamics.  

**Key Charts**
- **ETH → Linea Bridge Volume vs. Etherex Volume**  
  *Compares Ethereum inflows to Linea with on-chain Etherex activity.*  
  - Insight: Correlates cross-chain movement with protocol adoption.  
- **Average Trade Size & Daily Trading Activity**  
  *Tracks both overall activity levels and trading sophistication.*  
  - Insight: Highlights capital concentration patterns and liquidity depth.  

---
#### Staking-to-Swap Time Lag

**Description:**  
This chart measures the time elapsed between a user staking REX and subsequently executing a swap. It provides insight into how quickly users engage with the protocol after staking, highlighting user behavior and engagement patterns.

**Metrics Displayed:**  
- `users_with_time_lags`: Total number of users who staked and then swapped.  
- `avg_min_time_lag_minutes`: Average minimum time (in minutes) between staking and swap per user.  
- `median_time_lag_minutes`: Median minimum time between staking and swap.  
- `p90_time_lag_minutes`: 90th percentile minimum time between staking and swap.  
- `p99_time_lag_minutes`: 99th percentile minimum time between staking and swap.  

By structuring the dashboard around **Etherex stakeholders and ecosystem context**, the data serves **internal teams, external advisors, and end-users** alike—making it easier to connect **operational mechanics** with **strategic growth signals**.

## Methodology
### Data Collection Process

Main Contract Addresses:
0xefd81eec32b9a8222d1842ec3d99c7532c31e348 - REX token 
0xc93B315971A4f260875103F5DA84cB1E30f366Cc - xREX Staking
0x5C1Bf4B7563C460282617a0304E3cDE133200f70 - WETH/REX DEX POOL

### Chart Explanation
1. 
2.
3.
4. Evaluating Metrics for Emission Effectiveness
:unique_daily_stakers: It measures the number of distinct addresses staking REX tokens each day.
Relevance: Indicates how many unique users are participating in the staking mechanism, which is likely the source of incentives (e.g., rewards for staking).
Pros: Directly measures unique participants in the incentive system. Higher numbers suggest more users are engaging with staking, potentially motivated by rewards.
Cons: Doesn’t directly show trading activity, so it only represents the input (incentives) side.
Data Insight: Ranges from 1 (Aug 6) to 769 (Aug 7), dropping to 130 by Aug 29. This shows varying staking engagement, with a peak early on.

:unique_daily_traders: It measures the number of distinct addresses performing swaps on Etherex pairs each day.
Relevance: Represents unique users engaging in the desired activity (trading). If incentives work, we’d expect higher unique_daily_traders when staking is high.
Pros: Captures unique participants in the target activity, showing the breadth of DEX usage.
Cons: Doesn’t directly tie to staking, so we need to correlate it with staking metrics.
Data Insight: Ranges from 532 (Aug 6) to 2765 (Aug 7), stabilizing around 830–1385 by Aug 29. Trading engagement is consistently higher than staking.

:trader_to_staker_ratio: It measures the ratio of unique_daily_traders to unique_daily_stakers (i.e., how many unique traders exist per unique staker).
Relevance: Directly compares unique participants in trading vs. staking, indicating whether staking incentives attract more traders relative to stakers. A higher ratio suggests that staking (incentives) drives broader trading activity.
Pros: Combines both unique metrics into a single indicator of effectiveness. A high ratio (e.g., more traders per staker) implies incentives are successfully driving trading.
Cons: Can be skewed on days with low unique_daily_stakers (e.g., 532 on Aug 6 due to only 1 staker). It’s less meaningful if staking is zero or very low.
Data Insight: Spikes to 532 on Aug 6 (1 staker, 532 traders), then stabilizes at 2–8 (mostly 3–6) from Aug 7 onward. This suggests 2–8 unique traders per staker on most days.

:swaps_per_staked_token: It measures the number of swaps (daily_swaps) per unit of staked REX tokens (daily_staked).
Relevance: Shows how much trading activity occurs relative to the amount staked, linking incentives (staked tokens) to activity (swaps). Higher values suggest more trading per staked token.
Pros: Directly ties staking volume to trading volume, useful for assessing if larger stakes drive more swaps.
Cons: Doesn’t focus on unique participants, as daily_swaps includes repeated transactions by the same users. Also, it’s zero when daily_staked is zero.
Data Insight: Varies widely, from 0.0000044 (Aug 6) to 0.3853 (Aug 16). High values (e.g., Aug 15–16) occur when daily_staked is low, suggesting sensitivity to staking volume.

daily_staked and daily_swaps:What they measure: Total REX tokens staked and total swap transactions per day.
Relevance: Show the scale of staking and trading but don’t account for unique participants.
Cons: Can be inflated by a few active users, making them less suitable for measuring distinct engagement.

staking_transactions:What it measures: Total staking transactions per day.
Cons: Like daily_swaps, it includes repeated actions by the same users, not unique participants.



### SQL Queries & API Scripts

Challenges with Etherex:
Very Recent Launch - Limited historical data (only ~28 days in our database)
Sustainability Questions - Recent growth may be unsustainable

## Challenges
until the ABI for that contract is decoded, we can’t calculate actual fee amounts from the logs.
Decoded Event Data is Missing
Many of the newer contracts (e.g., FeeCollector, Pair contracts) are not yet decoded by Dune.
Key numeric fields such as amount, arg0, or token-specific data are unavailable.
Queries relying on bytearray_to_uint256 or arg0 fail or return 0 values.
Contract ABIs Not Fully Integrated
Without the ABI, we can only access general log metadata (block time, tx hash, event name).
Calculating USD value of swaps, fee payouts, or token transfers is impossible until ABI decoding is complete.

Workarounds Implemented
Event Counting Instead of Volume. For fee-related charts, we track the number of FeesCollected events and unique collectors. This provides a proxy metric for activity, even without numeric fee amounts. 
Current Status – xREX Fee Earnings
Available metric: Weekly counts of FeesCollected events across all FeeCollector contracts.
Unavailable metrics: Actual amounts of fees in REX tokens. The event data is not decoded yet.
Reason: New project, logs decoding not complete on Dune.
Workaround: Use event counts as a proxy for activity while waiting for decoded data. Once Dune exposes amount or value in decoded logs, the query can be upgraded to sum fee amounts per week.

## Resources
[Blockworks](https://blockworks.co/news/linea-previews-eth-first-roadmap)
[Cointelegraph](https://cointelegraph.com/news/consensys-launches-linea-zk-evm-to-scale-ethereum)
[DefiLlama](https://defillama.com/protocol/dexs/etherex)
DEXScreener ? https://dexscreener.com/linea/0x5c1bf4b7563c460282617a0304e3cde133200f70
[Dune Docs](https://docs.dune.com/home)
[Etherex Docs](https://docs.etherex.finance/)
[Linea official](https://linea.build/)
[Linea Block Explorer](https://lineascan.build/)

