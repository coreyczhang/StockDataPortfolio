import pandas as pd

# Read your stacked format file
df = pd.read_csv("multisymbol_test.csv", header=None, names=["Date", "Symbol", "Value"])

# Pivot to wide format
df_wide = df.pivot(index="Date", columns="Symbol", values="Value").reset_index()

# Save in correct format
df_wide.to_csv("multisymbol_test_wide.csv", index=False)