
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.figure_factory as ff


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
#Filter the Gap to 0.0009 Tick size
filter_gap = weekly_df1[(weekly_df1['Gap'] >= 0.0009) | (weekly_df1['Gap'] <= -0.0009)]

# Print the weekly data with the weekend gap
print(weekly_df1)

#Turn this into buy and sell signals

#Adds a new column for the signal
threshold = 0.0009 #Minimum pip movement of 9 pips.
filter_gap['Signal'] = 0  # Initialize Signal column to 0
filter_gap.loc[weekly_df1['Gap'] >= threshold, 'Signal'] = 1 # Long position signal
filter_gap.loc[weekly_df1['Gap'] <= -threshold, 'Signal'] = -1 # Short position signal

print("Gap filtered to 0.0009")
print(filter_gap)

#Linking the new module - backtesting
import backtesting
from backtesting import test
print(test)

