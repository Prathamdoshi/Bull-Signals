import requests
from datetime import *


#--------------------GLOBAL VARIABLES--------------------#

# list containing of the tickers we are watching out for
stock_tickers = ["AAPL", "TSLA", "AMZN", "GOOGL", "FB", "NFLX", "NVDA", "AMD", "GME", "SPCE"]

# variables to store the relative values of today and yesterday
today = date.today()
yesterday = today - timedelta(days = 1)

# data structure collectors set as global variables to be accessed by all the functions
stocks_yest = {}
stocks_today = {}
stock_alerts = {}
news_today = {}

#--------------------FUNCTIONS--------------------#
