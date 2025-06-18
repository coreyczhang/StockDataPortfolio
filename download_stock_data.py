import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# List of stock symbols
symbols = ['AAPL', 'TSLA', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'NFLX', 'JPM', 'BAC']

# Today's date and date 6 months ago
end_date = datetime.now()
start_date = end_date - timedelta(days=180)

# Loop through each stock symbol and save data
for symbol in symbols:
    data = yf.download(symbol, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    data = data[['Close']]  # Keep only the closing price
    data.reset_index(inplace=True)
    data['Symbol'] = symbol
    file_name = f"{symbol}_closing_prices.csv"
    data.to_csv(file_name, index=False)
    print(f"Saved: {file_name}")

# Placeholder to send to Precision Alpha
print("Now send these CSVs to Precision Alpha (not automated yet).")