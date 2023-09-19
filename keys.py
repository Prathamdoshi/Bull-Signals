ticker_to_company = {
    "NFLX": "Netflix, Inc.",
    "TSLA": "Tesla, Inc.",
    "NVDA": "NVIDIA Corporation",
    "AMD": "Advanced Micro Devices, Inc.",
    "GME": "GameStop Corp.",
    "SPCE": "Virgin Galactic Holdings, Inc.",
    "GOOGL": "Alphabet Inc."
}


STOCKS_API_KEY = "VIE96I33NUDH0HTL"
STOCKS_API_URL = "https://www.alphavantage.co/query?"

STOCKS_PARAM = {
    "function"  : "TIME_SERIES_DAILY",
    "Symbol"    : "",
    "apikey"    : STOCKS_API_KEY
}

TWILIO_ACCOUNT_SID = 'ACf83fa8ce30bef8fcc9757af90b05a18d'
TWILIO_ACCOUNT_AUTH = 'f00a1452fdab74d72148efa231d214cf'

NEWS_API = "921b2bc720574a2c88069fe3104863aa"
NEWS_API_URL = "https://newsapi.org/v2/everything?"

NEWS_PARAM = {
       "q"  : "",
    "from"  : "",
    "to": "",
    "sortBy": "popularity",
    "apiKey" : "921b2bc720574a2c88069fe3104863aa"
}