# Bull-Signals

## Introduction

Bull-Signals is a Python-based application designed to keep you updated on the stock prices of your top 10 companies. This project showcases a well-structured codebase, effective use of external APIs, and the skills acquired during its development.

## Code Design

The codebase is organized into functions, making it modular and easy to maintain. Here's an overview of the code's structure:

### Global Variables

- `stock_tickers`: A list of stock tickers to monitor.
- `today` and `yesterday`: Variables storing date information.
- `stocks_yest` and `stocks_today`: Dictionaries to hold stock prices.

### Functions

#### `fetch_stock()`

- Fetches stock data from the Alpha Vantage API.
- Updates `stocks_today` with opening prices for today.
- Updates `stocks_yest` with closing prices from yesterday.
- Demonstrates proficiency in making API requests with the `requests` library.

#### `send_alerts(stock, value, emoji, title, description)`

- Sends SMS alerts via Twilio for significant stock price changes.
- Utilizes the Twilio API for communication.
- Shows knowledge of integrating third-party services into Python applications.

#### `fetch_news(ticker, from_date, to_date)`

- Fetches news related to a specific stock using the Alpha Vantage News API.
- Provides the title and description of the top news article.
- Illustrates the ability to extract relevant data from API responses.

#### `compare_stocks()`

- Compares stock prices between today and yesterday.
- Calculates percentage change in stock prices.
- Triggers SMS alerts and fetches news for stocks with >2% price changes.
- Displays strong analytical and decision-making skills in stock monitoring.

### Main

- The main section orchestrates the flow of the program.
- Calls functions to fetch stock data, compare prices, and send alerts.
- Demonstrates a structured and organized approach to program execution.

## Technologies Used

- **Python**: The primary programming language used for this project.
- **Requests Library**: Used for making HTTP requests to the Alpha Vantage API.
- **Twilio API**: Employed for sending SMS alerts.
- **Alpha Vantage API**: Provides stock data and news information.
- **Datetime Module**: Utilized to manage date and time information effectively.

## Skills Acquired

During the development of Bull-Signals, several skills were honed and acquired:

- **API Integration**: Proficiency in integrating external APIs to gather real-time data.

- **Data Manipulation**: The ability to parse and process JSON data effectively.

- **Modular Code Design**: Structuring code into functions for reusability and maintainability.

- **Error Handling**: Handling errors gracefully, as demonstrated by the use of `raise_for_status()`.

- **Decision Making**: Making data-driven decisions to trigger alerts based on percentage changes.

- **Third-Party Services Integration**: Incorporating third-party services (Twilio) for additional functionality.

## Conclusion

Bull-Signals is not only a practical tool for stock monitoring but also a testament to your growing Python skills. The well-designed code, effective use of APIs, and the array of skills acquired make this project a valuable addition to your portfolio.
