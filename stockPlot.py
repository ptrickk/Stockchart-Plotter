#installed 'pip install matplotlib'
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import stockAPI

plt.style.use('seaborn')

symbol = input('Enter Symbol: ')

#interval: (5m | 15m | 1d | 1wk | 1mo)
#range:  ["1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"]
stockQuery = stockAPI.read(symbol,'1d','1y')
stockData = stockAPI.getValue(stockQuery)
stockAPI.printValue(stockData)

plt.plot_date(stockData[0], stockData[1], linestyle ='solid')
plt.tight_layout()
plt.show()