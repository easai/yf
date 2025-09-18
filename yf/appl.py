import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker and date range
ticker = yf.Ticker("AAPL")
data = ticker.history(start="2025-09-01", end="2025-09-18")

# Plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(data.index, data["Close"], marker='o', linestyle='-', color='blue')
plt.title("Apple (AAPL) Closing Prices - September 2025")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
