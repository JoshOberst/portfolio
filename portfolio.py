import numpy as np
import pandas as pd
from yahoofinancials import YahooFinancials
import yfinance as yf
import datetime as dt
import nasdaqdatalink as nl


stockList = ['AAPL','IBM','TSLA'] #list of stocks to analyse
benchmark = ['SPY']                 #benchmark stock ticker
startTime = dt.datetime(2010,1,1)   #start time of the data

#getting treasury rates
mydata = nl.get("USTREASURY/BILLRATES")
print(mydata.index)

#data = yf.download(benchmark+stockList,startTime).get('Adj Close')

#print(data)