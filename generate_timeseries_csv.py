import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Your portfolio (up to 25 symbols)
symbols = ['AAPL', 'TSLA', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'NFLX', 'JPM', 'BAC']

# 6 months back from today
end_date = datetime.today().date()
start_date = end_date - timedelta(days=180)

# Create a DataFrame with dates as index
combined_df = pd.DataFrame()

for symbol in symbols:
    print(f"Downloading {symbol}...")
    df = yf.download(symbol, start=start_date, end=end_date)[["Close"]]
    df.rename(columns={"Close": symbol}, inplace=True)  # Rename column to symbol
    if combined_df.empty:
        combined_df = df
    else:
        combined_df = combined_df.join(df, how="outer")

# Reset index to have 'Date' as a column
combined_df.reset_index(inplace=True)
combined_df.sort_values("Date", inplace=True)

# Save to CSV
combined_df.to_csv("precision_alpha_timeseries.csv", index=False, header=False)
print("✅ Saved in wide format: precision_alpha_timeseries.csv")