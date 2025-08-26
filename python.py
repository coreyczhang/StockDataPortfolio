import pandas as pd

# Load your long-format CSV file
df = pd.read_csv("precision_alpha_timeseries.csv", header=None)
df.columns = ["Date", "Symbol", "Value"]

# Pivot to wide format
df_wide = df.pivot(index="Date", columns="Symbol", values="Value").reset_index()

# Save to new CSV
df_wide.to_csv("precision_alpha_timeseries_wide.csv", index=False)