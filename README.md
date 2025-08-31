# Etherex Adoption Analysis
Beyond Volume Metrics - Tracking real activity metrics on Linea's fastest-rising Decentralised Exchange (DEX)

## Table of Contents

1. [Introduction](#introduction)
2. [Dashboard Overview](#dashboard-overview)
3. [Methodology](#methodology)
4. [Key Insights](#Key-insights)
5. [Challenges](#challenges)
5. [Resources & References](#resources--references)
  
## 1. Introduction
### Project Overview

Welcome to the Etherex Dashboard, a comprehensive analytics tool examining genuine user engagement on Etherex, Linea's native DEX, while filtering out bot manipulation and vanity metrics.

#### Why Linea & Etherex
**Linea**: ConsenSys' zkEVM rollup is gaining significant traction as a high-performance L2 solution, with accelerating adoption in the Ethereum scaling landscape.

**Etherex**: Currently the second-largest DEX on Linea by TVL (Total Value Locked), powered by metaDEX x(3,3) methodology—an evolved, more accessible version of ve(3,3).

#### What Makes Etherex Unique
* 100% fee distribution → All trading fees to stakers
* 100% liquidity rewards → All rewards goes to Liquidy Providers, no team cuts
* REX flywheel → LPs earn REX → Stake as xREX for governance + fee sharing


This analysis explore real, actionable metrics in a fast-growing ecosystem, providing insights into both protocol health and broader L2 adoption trends.

Sources: [Blockworks](https://blockworks.co/news/linea-previews-eth-first-roadmap) / [Cointelegraph](https://cointelegraph.com/news/consensys-launches-linea-zk-evm-to-scale-ethereum) / [DefiLlama](https://defillama.com/protocol/dexs/etherex) / [Etherex Twitter](https://x.com/etherexfi/status/1947132627737309399)

## 2. Dashboard Overview
The Etherex Dashboard provides a structured view of the protocol’s performance within the Linea ecosystem. Charts are created for different stakeholder audiences — **Protocol Teams, Advisors, and Users** — to deliver actionable insights.

Data is sourced from **Dune Analytics** and presented with a balance of technical accuracy and strategic interpretation.

| Dashboard Sections    | Charts                                                       | Audience / Purpose |
| -------------------- | ------------------------------------------------------------ | ------------------ |
| Protocol Performance | Daily REX Staking, Emission Effectiveness, Staking-to-Swap   | Protocol Teams     |
| User Behaviour        | User Quality Analysis, User Leaderboard                      | Advisors / Users   |
| Trading & Adoption   | Top Trading Pairs, Etherex Adoption & Sustainability Metrics | Advisors / Users   |

---

You can access the full dashboard [here](https://dune.com/kukumaster/etherex).

### Chart Descriptions

- **Daily REX Staking** – Monitors staking adoption and conversion to xREX. Useful for protocol teams to assess incentive uptake.  
- **Emission Effectiveness** – Compares staking to DEX activity to measure incentive efficiency. Mainly for protocol teams.  
- **Staking-to-Swap Time Lag** – Tracks how quickly staking translates into swaps, showing incentive effectiveness. Protocol-focused.  
- **User Quality Analysis** – Distinguishes real vs. bot users, useful for subscribers and protocols to understand genuine adoption.  
- **User Leaderboard** – Ranks users by activity and volume; relevant for subscribers and protocol teams tracking engagement.  
- **Top Trading Pairs by Activity Score** – Shows the most active trading pairs; mainly for protocol teams to monitor liquidity.  
- **Etherex Adoption & Sustainability Metrics** – Aggregated adoption, retention, and sustainability indicators; valuable for advisors, protocol teams, and users.

---

By structuring the dashboard around Etherex stakeholders and ecosystem context, the data serves internal teams, external advisors, and end-users alike, making it easier to connect operational mechanics with strategic growth signals.

## Methodology
### Data Collection Process
...???

Main Contract Addresses:
0xefd81eec32b9a8222d1842ec3d99c7532c31e348 - REX token 
0xc93B315971A4f260875103F5DA84cB1E30f366Cc - xREX Staking
0x5C1Bf4B7563C460282617a0304E3cDE133200f70 - WETH/REX DEX POOL

### Chart Explanation
My analysis of user behavior around the Etherex protocol uses two complementary measurement lenses:
1. Token Transfer Analysis (ERC‑20)
 - Based on REX token transfers recorded from the ERC‑20 contract.
 - Metrics: total tokens sent, average transfer size, unique counterparties, activity span.
 - Purpose: to capture the economic weight of wallets — i.e., who is actually moving meaningful amounts of REX.
 - Example classification:
Dust Bots = wallets with high transfer counts but average transfer size < 1 REX, typically negligible in overall token flow (`WHEN avg_transaction_size < 1 AND total_transactions > 20 THEN 'Dust Bot`)

2. DEX Swap Analysis (behavioral focus)
 - Based on swap logs from Etherex liquidity pools on Linea.
 - Metrics: trade counts, pairs traded against, number of active days, activity span.
 - Purpose: to capture the behavioral footprint of wallets — i.e., who is most active by raw trading frequency.
 - Example classification:
Dust Bots = wallets with many trades but very low average trades/day or consistent low‑value spam activity (`WHEN avg_trade_per_day < 1 AND number_of_trades > 20 THEN 'Dust Bot`)

Why Two Definitions of "Dust Bots"?
The term Dust Bot is deliberately used in both contexts, but with different operational definitions, because the analysis is meant to compare economic impact vs behavioral activity:
In token transfer space, Dust Bots contribute almost no volume and are economically insignificant.
In trading activity space, Dust Bots dominate trade counts, highlighting their role as network spam rather than meaningful participants.

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
Very Recent Launch - Limited historical data (only ~28 days in our database). Etherex Dune tables don’t provide USD amounts because the logs are not decoded.
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
I tired a Python-based solution that decodes the raw logs using the known ABI of Swap events. This shows Data sourcing & independence: I am identifying missing data and figuring out alternative ways to get it.
Problem-solving: I am using Python to reconstruct USD volumes when the SQL source is incomplete.
Current Status – xREX Fee Earnings
Available metric: Weekly counts of FeesCollected events across all FeeCollector contracts.
Unavailable metrics: Actual amounts of fees in REX tokens. The event data is not decoded yet.
Reason: New project, logs decoding not complete on Dune.
Workaround: Use event counts as a proxy for activity while waiting for decoded data. Once Dune exposes amount or value in decoded logs, the query can be upgraded to sum fee amounts per week.

## Resources
[Blockworks](https://blockworks.co/news/linea-previews-eth-first-roadmap) |
[Cointelegraph](https://cointelegraph.com/news/consensys-launches-linea-zk-evm-to-scale-ethereum) |
[DefiLlama](https://defillama.com/protocol/dexs/etherex) |
[DEXScreener](https://dexscreener.com/linea/0x5c1bf4b7563c460282617a0304e3cde133200f70) |
[Dune Docs](https://docs.dune.com/home) |
[Etherex Docs](https://docs.etherex.finance/) |
[Linea Docs](https://docs.linea.build/technology/canonical-token-bridge) |
[Linea official](https://linea.build/) |
[Linea Block Explorer](https://lineascan.build/) 

