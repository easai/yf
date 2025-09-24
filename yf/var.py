import yfinance as yf
import numpy as np

def get_daily_returns(ticker, period="1y"):
    """
    Fetch historical daily returns for a given ticker.
    """
    data = yf.download(ticker, period=period, group_by='column')  # flatten columns
    if data.empty:
        raise ValueError(f"No data returned for ticker '{ticker}'.")

    # If 'Adj Close' is missing, fallback to 'Close'
    price_column = 'Adj Close' if 'Adj Close' in data.columns else 'Close'
    data['Daily Return'] = data[price_column].pct_change()
    return data['Daily Return'].dropna()

def calculate_var(returns, confidence_level=0.99, portfolio_value=1_000_000):
    """
    Calculate historical VaR.
    """
    sorted_returns = np.sort(returns)
    index = int((1 - confidence_level) * len(sorted_returns))
    var_percent = abs(sorted_returns[index])
    return var_percent * portfolio_value

# Example usage
if __name__ == "__main__":
    ticker = "SPY"
    confidence = 0.99
    portfolio_val = 1_000_000

    try:
        returns = get_daily_returns(ticker)
        var = calculate_var(returns, confidence, portfolio_val)
        print(f"{int(confidence*100)}% Historical VaR for {ticker}: ${var:,.2f}")
    except Exception as e:
        print(f"Error: {e}")
