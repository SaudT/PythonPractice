import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web


style.use('ggplot')

# video part 1
start = dt.datetime(2020,3,8)
end = dt.datetime(2020, 8, 9)

ticker = input("What stock do you want to see: ")

df = web.DataReader(ticker, 'yahoo', start, end)  

df.to_csv('stock.csv')

#df = pd.read_csv('stock.csv', parse_dates = True, index_col=0)  #not sure what this line does
print(df.head(15))
print()
print(df.tail(30))

# video part 2   # Review video part 2
# print(df.head())

df['Adj Close'].plot()
plt.show()

# 100 moving average. Moving average, takes average of last 100 days to see if the next days 100 day average is trending which way
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()


