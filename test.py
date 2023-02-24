
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

#Importing data
def download(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df

df1 = download("EURUSD=X", "2003-12-1", "2023-03-06",)
df1 = df1.loc[:, ["Open", "Close"]]  # Sets out only Open and close prices in the dataset.
weekly_df1 = df1.resample("W").agg({'Open': 'first', 'Close': 'last'})
weekly_df1.head() #Above, filters data to weekly. Sunday open to Friday close.
print(weekly_df1.head)

#Work out how to do the gap + display

weekly_df1['Gap'] = weekly_df1['Open'].shift(-1) - weekly_df1['Close'] #-1 to use the open of the next week.

# Print the weekly data with the weekend gap
print(weekly_df1)

#Plotting figures
plt.figure(figsize=(15, 7))
df1['Close'].plot()
weekly_df1['Close'].plot()
# Set the title and axis label
plt.title('EUR/USD Data', fontsize=16)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Price', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(['Daily Close', 'Weekly Close'], prop={'size': 15})
# Show the plot
plt.show()

#Filter the Gap 0.0001 Tick size
filter_gap =
#Turn this into buy and sell signals
#backtest it ->  Look Matts backtesting