import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Date: The date of the data point.
# Open: The opening price of Bitcoin for that day.
# High: The highest price of Bitcoin for that day.
# Low: The lowest price of Bitcoin for that day.
# Close: The closing price of Bitcoin for that day.
# Adj Close: The adjusted closing price of Bitcoin for that day (which can sometimes account for dividend payments or stock splits, but in the case of Bitcoin, it's usually the same as the Close price).
# Volume: The trading volume of Bitcoin for that day.
bitcoin = pd.read_csv('BTC-USD.csv')
bitcoin['Date'] = pd.to_datetime(bitcoin['Date'])
print(bitcoin.head())

VOO = pd.read_csv('VOO.csv')
VOO['Date'] = pd.to_datetime(VOO['Date'])
print(VOO.head())

plt.tight_layout()
plt.show()
