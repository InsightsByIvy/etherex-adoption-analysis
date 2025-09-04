import requests
import pandas as pd
from pycoingecko import CoinGeckoAPI
from datetime import datetime
from tqdm import tqdm
from dune_client.client import DuneClient
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# 1. Configuration
DUNE_API_KEY = os.getenv("DUNE_API_KEY")  

# 1. Configuration
dune = DuneClient(DUNE_API_KEY)

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


# Initialise CoinGecko API client
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

# Preview data
print(logs[['date', 'Daily REX Volume', 'usd_volume']].head())

# Ensure the folder exists
os.makedirs("Images", exist_ok=True)


# Plot Daily REX Volume 
fig, ax1 = plt.subplots(figsize=(12,6))

color1 = '#03141F'
ax1.bar(logs['date'], logs['Daily REX Volume'], color=color1, label='Daily REX Volume')
ax1.set_xlabel("Date")
ax1.set_ylabel("Daily REX Volume (tokens)", color=color1)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax1.grid(True, which='major', axis='y', linestyle='--', alpha=0.5)
plt.xticks(rotation=45)

# Plot USD volume 
color2 = '#54BAFF'  
ax2 = ax1.twinx()
ax2.plot(logs['date'], logs['usd_volume'], color=color2, marker='o', linewidth=2, label='USD Volume')
ax2.set_ylabel("USD Volume (USD)", color=color2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))

# Title and legend
plt.title("Daily REX Volume (tokens & USD)", fontsize=14, fontweight='bold')
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc="upper right", frameon=False)

fig.tight_layout()
plt.savefig("Images/daily_rex_volume.png", dpi=300, bbox_inches='tight')
plt.show()

print("Chart saved to Images/daily_rex_volume.png")

