#!/usr/bin/python3
# Ref: https://matplotlib.org/api/finance_api.html

import pandas as pd
import numpy as np
import talib
from mpl_finance import candlestick_ohlc


import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Avoid FutureWarning: Pandas will require you to explicitly register matplotlib converters.
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Load data from CSV file.
##########################
my_headers = ['date', 'open', 'high', 'low', 'close', 'volume']
my_dtypes = {'date': 'str', 'open': 'float', 'high': 'float', 'low': 'float',
             'close': 'float', 'volume': 'float'}
my_parse_dates = ['date']
loaded_data = pd.read_csv('sp500.csv', sep=',', header=1, names=my_headers,
                          dtype=my_dtypes, parse_dates=my_parse_dates)

# Convert 'Timestamp' to 'float'.
#   candlestick_ohlc needs time to be in float days format - see date2num().
loaded_data['date'] = [mdates.date2num(d) for d in loaded_data['date']]

# Re-arrange data so that each row contains values of a day: 'date','open','high','low','close'.
quotes = [tuple(x) for x in loaded_data[['date', 'open', 'high', 'low', 'close']].values]

# Plot candlestick.
##########################
fig, ax = plt.subplots()
candlestick_ohlc(ax, quotes, width=0.5, colorup='g', colordown='r');

# Customize graph.
##########################
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock')

# Format time.
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

plt.gcf().autofmt_xdate()  # Beautify the x-labels
plt.autoscale(tight=True)

plt.show()
