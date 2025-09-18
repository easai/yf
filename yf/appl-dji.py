import yfinance as yf
import matplotlib.pyplot as plt

# Define date range
start_date = "2025-09-01"
end_date = "2025-09-18"

# Download data
aapl = yf.Ticker("AAPL").history(start=start_date, end=end_date)
dji = yf.Ticker("^DJI").history(start=start_date, end=end_date)

# Create plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot AAPL on primary y-axis
ax1.plot(aapl.index, aapl["Close"], color="blue", marker="o", label="AAPL")
ax1.set_xlabel("Date")
ax1.set_ylabel("AAPL Closing Price (USD)", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")
ax1.grid(True)

# Create secondary y-axis for Dow Jones
ax2 = ax1.twinx()
ax2.plot(dji.index, dji["Close"], color="green", marker="s", label="Dow Jones (^DJI)")
ax2.set_ylabel("Dow Jones Closing Price (USD)", color="green")
ax2.tick_params(axis="y", labelcolor="green")

# Title and layout
plt.title("AAPL vs Dow Jones - Closing Prices (Sep 2025)")
fig.tight_layout()
plt.xticks(rotation=45)
plt.show()
