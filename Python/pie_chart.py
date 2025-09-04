import pandas as pd
import matplotlib.pyplot as plt
from dune_client.client import DuneClient
import os
from dotenv import load_dotenv


# Load .env variables
load_dotenv()

# 1. Configuration
DUNE_API_KEY = os.getenv("DUNE_API_KEY")  
if not DUNE_API_KEY:
    raise ValueError("DUNE_API_KEY not found in environment variables")

QUERY_ID = 5726091     # Leaderboard query ID

print("API Key loaded:", DUNE_API_KEY)

# Initialise Dune client
dune = DuneClient(DUNE_API_KEY)



# 2. Fetch results
query_result = dune.get_latest_result(QUERY_ID)
df = pd.DataFrame(query_result.result.rows)

# 2. Load Dune results
logs = pd.DataFrame(query_result.result.rows)
print("Columns in query:", logs.columns.tolist())
print("Rows returned:", len(logs))

# 3. User Type Distribution Pie Chart
user_type_counts = logs['user_type'].value_counts()

# Plot pie chart
plt.figure(figsize=(6, 4))
plt.pie(
    user_type_counts,
    labels=None,  
    autopct='%1.1f%%',  # Show percentages on slices
    startangle=90,
    colors=['#606C38', "#F5E536", '#FEFAE0', '#283618', '#FF6B6B', '#BC6C25', "#C655AF", "#6B7CDE"]  
)
plt.title("Etherex User Type Distribution")

# Add legend separately
plt.legend(
    labels=user_type_counts.index,
    loc="center left",  
    bbox_to_anchor=(1.1, 0.5),  # move legend outside to the right
    title="User Types",
    prop={'size': 8},        
    title_fontsize=9         
)

plt.tight_layout()

# Ensure Images folder exists
os.makedirs("Images", exist_ok=True)
plt.savefig("Images/user_type_distribution.png", dpi=300)
plt.show()