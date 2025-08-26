# StockDataPortfolio

StockDataPortfolio is a workflow for downloading, organizing, and analyzing stock time-series data with Precision Alpha’s Decision Machine platform. It helps create properly formatted CSVs and configuration files for both binary (up/down) and unit-based analyses.

## Features
- Download and organize daily closing price data for individual tickers or multi-symbol portfolios.  
- Generate CSVs compatible with Precision Alpha batch jobs.
    - `config_*.ini` → binary up/down movement analysis  
    - `measure_*.ini` → value-based analysis  
- Create config files for binary analysis and measure files for value-based analysis.  
- Merge stock data for multi-symbol portfolio backtesting.  
- Automate parts of the data preparation process with included Python scripts.  

## Usage
1. Install dependencies:  pip install -r requirements.txt
2. Edit ticker symbols in `download_stock_data.py` and run to fetch raw data.  
3. Run `generate_timeseries_csv.py` to produce formatted CSV files.  
4. Upload the generated CSVs along with config and measure files to the Precision Alpha Decision Machine S3 bucket.  

## Next Steps
- Automate batch uploads to S3.  
- Add plotting and visualization of analysis results.  
- Explore similarity search and embeddings for report analysis.  

## References
- Precision Alpha Decision Machine documentation  
- Self-Service Data Dictionary (June 2025) included in repository  
