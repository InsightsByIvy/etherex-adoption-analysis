import requests
import pandas as pd
from pycoingecko import CoinGeckoAPI
from datetime import datetime
from tqdm import tqdm
from dune_client.client import DuneClient

# 1. Configuration
dune = DuneClient("Xsfx6F1nmzvQV3GcosoflC3AO06yqh3r")

# Adoption & Sustainability query
QUERY_ID = 5706649
query_result = dune.get_latest_result(QUERY_ID)

# 2. Load Dune results
logs = pd.DataFrame(query_result.result.rows)
print("Columns in query:", logs.columns.tolist())
print("Rows returned:", len(logs))

# Ensure 'date' column is datetime
if 'date' in logs.columns:
    logs['date'] = pd.to_datetime(logs['date'])
     # Keep as datetime internally, but remove time and timezone for display
    logs['date'] = logs['date'].dt.date
else:
    raise ValueError("No 'date' column found in query result")
print("Date range in data:", logs['date'].min(), "to", logs['date'].max())


# Initialize CoinGecko API client
cg = CoinGeckoAPI()

# Fetch the current price of REX in USD
prices = cg.get_price(ids=["etherex"], vs_currencies="usd")

# Extract the USD price
rex_usd = prices['etherex']['usd']

print(f"Current REX price in USD: ${rex_usd}")

if 'Daily REX Volume' in logs.columns:
    logs['usd_volume'] = logs['Daily REX Volume'] * rex_usd
else:
    print("Warning: 'Daily REX Volume' column not found. USD enrichment skipped.")



import matplotlib.pyplot as plt

ax = logs.plot(
    x='date',
    y=['Daily REX Volume', 'usd_volume'],
    kind='bar',
    figsize=(12,6)
)
ax.set_xlabel("Date")
ax.set_ylabel("Volume (millions of REX)")
ax.set_title("Daily REX Volume (tokens & USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.savefig("daily_rex_volume.png", dpi=300, bbox_inches='tight')

