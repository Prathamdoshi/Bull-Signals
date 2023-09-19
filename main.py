import requests
import keys
from datetime import *
from twilio.rest import Client


#--------------------GLOBAL VARIABLES--------------------#

# list containing of the tickers we are watching out for
stock_tickers = ["NFLX", "TSLA"]
# "NFLX", "NVDA", "AMD", "GME", "SPCE","GOOGL"

# variables to store the relative values of today and yesterday
today = date.today()
yesterday = today - timedelta(days = 1)

# data structure collectors set as global variables to be accessed by all the functions
stocks_yest = {"NFLX":250,"GOOGL":250}
stocks_today = {"NFLX":270,"GOOGL":230}


#--------------------FUNCTIONS--------------------#
def fetch_stock():

    # loop through stocks
    for stock in stock_tickers:

        # update the param with current stock, get the data, raise errors if any
        keys.STOCKS_PARAM["symbol"] = stock
        stock_reponse = requests.get(url=keys.STOCKS_API_URL, params=keys.STOCKS_PARAM)
        stock_reponse.raise_for_status()

        # add opening price of the stock
        stocks_today[stock] = stock_reponse.json()["Time Series (Daily)"][str(today)]["1. open"]

        # if today is monday then yesterday will be set to friday's date
        if datetime.now().weekday() == 0:

            yesterday =  today - timedelta(days=3)

        # add stock's closing price from yesterday
        stocks_yest[stock] = stock_reponse.json()["Time Series (Daily)"][str(yesterday)]["4. close"]

def send_alerts(stock,value,emoji,title,description):

    account_sid = 'ACf83fa8ce30bef8fcc9757af90b05a18d'
    auth_token = 'a66a3408837539a0736ec39202ccf0b0'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+18445591173',
        to='+14085505024',
        body= f"{stock}: {emoji} {abs(value)}%\nHeadline:{title}\nDescription:{description}"
    )

    print(message.sid)

def fetch_news(ticker,from_date,to_date):

    news = "potty"
    keys.NEWS_PARAM["from"] = from_date
    keys.NEWS_PARAM["to"] = to_date
    keys.NEWS_PARAM["q"] = keys.ticker_to_company[ticker]

    news_response = requests.get(url=keys.NEWS_API_URL,params=keys.NEWS_PARAM)
    title = news_response.json()['articles'][0]["title"]
    description = news_response.json()['articles'][0]["description"]

    return [title,description]

def compare_stocks():

    # loop through today's stocks
    for stock,price in stocks_today.items():

        # calculate diff of stock prices and convert its percentage
        delta = (price - stocks_yest[stock])
        delta_percent =  (delta / stocks_yest[stock]) * 100

        # if delta change in price is greater than 2% then trigger notifications
        if int(delta_percent) > 2:

            news = fetch_news(stock, yesterday, today)
            send_alerts(stock,delta_percent,"🔼 🟩",news[0],news[1])

        elif int(delta_percent) < -2:

            news = fetch_news(stock, yesterday, today)
            send_alerts(stock, delta_percent, "⬇️ 🔴",news[0],news[1])


#--------------------MAIN--------------------#\
if __name__ == '__main__':

   # fetch_stock()

    print(stocks_yest)
    print(stocks_today)

    compare_stocks()

