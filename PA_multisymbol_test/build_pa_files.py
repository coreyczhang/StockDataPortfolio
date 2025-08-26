
import sys
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def build_pa_files(symbols, outfile_prefix="csvdata"):
    end = datetime.today()
    start = end - timedelta(days=180)  # ~6 months

    data = yf.download(symbols, start=start, end=end)["Close"]
    if isinstance(data, pd.Series):
        data = data.to_frame()

    # Reset index and format date
    data.reset_index(inplace=True)
    data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')

    # Reorder so Date is first column
    cols = ["Date"] + [c for c in data.columns if c != "Date"]
    data = data[cols]

    # Save PA-ready CSV (no header)
    csv_file = f"{outfile_prefix}.csv"
    data.to_csv(csv_file, index=False, header=False)
    print(f"Wrote {csv_file}")

    # Build Measurements line
    measurements = ",".join([c for c in data.columns if c != "Date"])

    # Config (Binary)
    config_file = f"config_{outfile_prefix}.ini"
    with open(config_file, "w") as f:
        f.write("[Default]\n")
        f.write("FileOutput = output.customer.decision-machine.com/y37FjKZ5Fr\n")
        f.write(f"Measurements = {measurements}\n")
        f.write("Memory = 0\n")
        f.write("MemoryCount = 1\n")
        f.write("PostConfig = 0\n\n")
        f.write("[Binary]\n")
        f.write("T_R = 0.68\n")
    print(f"Wrote {config_file}")

    # Measure (Units)
    measure_file = f"measure_{outfile_prefix}.ini"
    with open(measure_file, "w") as f:
        f.write("[Default]\n")
        f.write("FileOutput = output.customer.decision-machine.com/y37FjKZ5Fr\n")
        f.write(f"Measurements = {measurements}\n")
        f.write("Memory = 0\n")
        f.write("MemoryCount = 1\n")
        f.write("PostConfig = 0\n")
    print(f"Wrote {measure_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python build_pa_files.py SYMBOL1 SYMBOL2 ...")
        sys.exit(1)
    symbols = sys.argv[1:]
    build_pa_files(symbols)
