test = print("test of linked module")

print(test)
#Backtest it ->  Look at Matts backtesting
##signals = weekly_df1['Signal'].tolist()
# Backtest the trading strategy

#Plotting figures - Hidden for now
#plt.figure(figsize=(15, 7))
#df1['Close'].plot()
#weekly_df1['Close'].plot()
# Set the title and axis label
#plt.title('EUR/USD Data', fontsize=16)
#plt.xlabel('Year', fontsize=15)
#plt.ylabel('Price', fontsize=15)
#plt.xticks(fontsize=15)
#plt.yticks(fontsize=15)
#plt.legend(['Daily Close', 'Weekly Close'], prop={'size': 15})
# Show the plot
#plt.show()
##returns = backtest(signals, weekly_df1)
# Define the backtest function
##def backtest(signals, price_data):
   ## positions = []  # initialize an empty list to store the positions
    ##for i in range(len(signals)):
       ## if signals[i] == 'Long':  # if the signal is long, buy at the open price
            ##positions.append(price_data['Open'][i])
        ##elif signals[i] == 'Short':  # if the signal is short, sell at the open price
            ##positions.append(-price_data['Open'][i])
       ## else:  # if there is no signal, hold the position
          ##  positions.append(0)
    # Calculate the returns of the strategy
   ## returns = np.diff(positions)
    ##return returns

# Apply the backtest function

# Calculate the cumulative returns and plot the results
##cumulative_returns = np.cumsum(returns)
##plt.plot(cumulative_returns)
##plt.title('Cumulative Returns of Weekend Gap Strategy')
##plt.xlabel('Week')
##plt.ylabel('Returns')