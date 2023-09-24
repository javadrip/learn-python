STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

import os
from datetime import date, timedelta

import requests
from dotenv import load_dotenv

load_dotenv()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_endpoint = "https://www.alphavantage.co/query"
stock_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
}

stock_response = requests.get(stock_endpoint, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

today = date.today()
yesterday = str(today - timedelta(days=2))

yesterday_open_price = float(stock_data["Time Series (Daily)"][yesterday]["1. open"])
yesterday_close_price = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])

percentage_change = round(
    ((yesterday_close_price / yesterday_open_price) * 100) - 100, 2
)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_query = COMPANY_NAME.replace(" ", "-").lower()

news_endpoint = "https://newsapi.org/v2/everything"
news_api_key = os.getenv("NEWS_API_KEY")
news_parameters = {"apiKey": news_api_key, "q": news_query, "from": yesterday}

news_response = requests.get(news_endpoint, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

first_three_articles = news_data["articles"][:3]

snippets = []

for article in first_three_articles:
    snippet = {}
    snippet["headline"] = article["title"]
    snippet["brief"] = article["description"]
    snippets.append(snippet)

print(snippets)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


for snippet in snippets:
    if percentage_change > 4:
        print(f"{STOCK}: 🔺{percentage_change}")
        print(f"Headline: {snippet['headline']}")
        print(f"Brief: {snippet['brief']}")
    elif percentage_change < -4:
        print(f"{STOCK}: 🔻{abs(percentage_change)}")
        print(f"Headline: {snippet['headline']}")
        print(f"Brief: {snippet['brief']}")

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
