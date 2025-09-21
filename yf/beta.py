import yfinance as yf
import numpy as np
import pandas as pd

# Define tickers and time range
stock_ticker = "MSFT"
market_ticker = "^GSPC"  # S&P 500
start_date = "2022-01-01"
end_date = "2023-01-01"

# Download historical data
stock_data = yf.download(stock_ticker, start=start_date, end=end_date, auto_adjust=True)
market_data = yf.download(market_ticker, start=start_date, end=end_date, auto_adjust=True)

# Calculate daily returns
stock_returns = stock_data["Close"].pct_change().dropna()
market_returns = market_data["Close"].pct_change().dropna()

# Align dates
combined = pd.concat([stock_returns, market_returns], axis=1)
combined.columns = ["Stock", "Market"]
combined.dropna(inplace=True)

# Calculate beta
cov_matrix = np.cov(combined["Stock"], combined["Market"])
beta = cov_matrix[0, 1] / cov_matrix[1, 1]

print(f"Beta of {stock_ticker} vs {market_ticker}: {beta:.4f}")
