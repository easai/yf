import yfinance as yf

ticker = yf.Ticker("AAPL")

data = ticker.history(period="1mo")
print(data)


print(ticker.financials)       # Income statement
print(ticker.balance_sheet)    # Balance sheet
print(ticker.cashflow)         # Cash flow
print(ticker.dividends)        # Dividend history
print(ticker.actions)          # Splits & dividends

info = ticker.info
print(info["sector"], info["marketCap"])
