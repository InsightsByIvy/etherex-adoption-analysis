import pandas as pd
import matplotlib.pyplot as plt
from dune_client.client import DuneClient
import os

# 1. Configuration
API_KEY = "Xsfx6F1nmzvQV3GcosoflC3AO06yqh3r"  
QUERY_ID = 5726091              # Leaderboard query ID

# Initialise Dune client
dune = DuneClient(API_KEY)

# 2. Fetch results
query_result = dune.get_latest_result(QUERY_ID)
df = pd.DataFrame(query_result.result.rows)

# 2. Load Dune results
logs = pd.DataFrame(query_result.result.rows)
print("Columns in query:", logs.columns.tolist())
print("Rows returned:", len(logs))

# 3. Top 10 users by weighted score
top_users = logs.sort_values(by='weighted_score', ascending=False).head(10)

# Keep only relevant columns
top_users_table = top_users[['leaderboard_rank', 'user_address', 'total_trades', 'active_days', 'total_gas_eth', 'weighted_score', 'user_type']]

# Show top 10 in terminal
print(top_users_table.head(10))

# Optionally, save full table as CSV
os.makedirs("Images", exist_ok=True)

# 4. User Type Distribution Pie Chart
user_type_counts = logs['user_type'].value_counts()

# Plot pie chart
plt.figure(figsize=(6, 4))
plt.pie(
    user_type_counts,
    labels=None,  
    autopct='%1.1f%%',  # Show percentages on slices
    startangle=90,
    colors=['#606C38', '#DDA15E', '#FEFAE0', '#283618', '#FF6B6B', '#BC6C25']  
)
plt.title("Etherex User Type Distribution")

# Add legend separately
plt.legend(
    labels=user_type_counts.index,
    loc="center left",  
    bbox_to_anchor=(1.1, 0.5),  # move legend outside to the right
    title="User Types",
    prop={'size': 8},         # shrink legend text
    title_fontsize=9          # shrink legend title
)

plt.tight_layout()

# Ensure Images folder exists
os.makedirs("Images", exist_ok=True)
plt.savefig("Images/user_type_distribution.png", dpi=300)
plt.show()