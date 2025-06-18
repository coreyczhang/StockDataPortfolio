import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

# Step 1: Define your 10-stock portfolio
symbols = ['AAPL', 'TSLA', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'NFLX', 'JPM', 'BAC']

# Step 2: Set date range (6 months)
end_date = datetime.today().date()
start_date = end_date - timedelta(days=180)

# Step 3: Prepare a DataFrame to hold all the results
all_data = pd.DataFrame()

# Step 4: Download & combine
for symbol in symbols:
    print(f"Fetching: {symbol}")
    data = yf.download(symbol, start=start_date, end=end_date)
    data = data[['Close']].copy()
    data.reset_index(inplace=True)
    data['Symbol'] = symbol
    data = data.rename(columns={'Date': 'Date', 'Close': 'Close'})
    all_data = pd.concat([all_data, data[['Date', 'Symbol', 'Close']]])

# Step 5: Sort & save
all_data.sort_values(by=['Date', 'Symbol'], inplace=True)
output_file = "precision_alpha_ready.csv"
all_data.to_csv(output_file, index=False)

print(f"\n✅ Done! Data saved to: {output_file}")