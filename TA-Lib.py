import numpy as np
import talib
import matplotlib.pyplot as plt

data = np.genfromtxt('sp500.csv', dtype=None, delimiter=',', names=True, encoding=None)

date_before_process = data['Date']
openp = data['Open']
highp = data['High']
lowp = data['Low']
closep = data['Close']
volume = data['Volume']

date_after_process = np.asarray(date_before_process, dtype='datetime64')

WMA = talib.WMA(closep, timeperiod=20)
SMA = talib.SMA(closep, timeperiod=20)
EMA = talib.SMA(closep, timeperiod=20)
OBV = talib.OBV(closep, np.asarray(volume, dtype='float'))
RSI = talib.RSI(closep, timeperiod=20)


# plt.plot(WMA)
# plt.plot(SMA)
# plt.plot(EMA)
# plt.plot(OBV)
# plt.plot(RSI)

# plt.plot(closep)
# plt.show()

