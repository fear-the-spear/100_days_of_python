import requests
from twilio.rest import Client
import datetime
from PRIVATE.variables import *
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc."
TODAY = str(datetime.datetime.today()).split()[0]
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day

av_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "interval": "60min",
    "datatype": "json",
    "apikey": ALPHA_VANTAGE_API_KEY
}

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before
#   yesterday then print("Get News").
av_response = requests.get(
    "https://www.alphavantage.co/query", params=av_params)
av_response.raise_for_status()
av_data = av_response.json()

new_list = [value for key, value in av_data["Time Series (Daily)"].items()]

yesterday_close = float(new_list[0]["4. close"])
day_before_yesterday_close = float(new_list[1]["4. close"])

change = "⬆️"
if yesterday_close >= day_before_yesterday_close:
    increase = yesterday_close - day_before_yesterday_close
    percent_change = round((increase / day_before_yesterday_close) * 100, 0)
else:
    change = "⬇️"
    decrease = day_before_yesterday_close - yesterday_close
    percent_change = round((decrease / day_before_yesterday_close) * 100, 0)

# STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the
    #   COMPANY_NAME.
news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "from": f"{year}-{month}-{day - 1}"
}
news_response = requests.get(
    "https://newsapi.org/v2/everything", params=news_params)
list_of_articles = news_response.json()["articles"]
headline = list_of_articles[0]["title"]
brief = list_of_articles[0]["description"]
link = list_of_articles[0]["url"]
msg_body = f"{STOCK} {change} {percent_change}%\n{headline}\n{brief}\nRead More: {link}"

if percent_change >= 0:
    print("Yes")
    # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=msg_body,
        # for some reason, twilio thinks this message is too long
        #   but the code is written just fine! If you want to get the
        #   message to send, make it a really short message
        from_=TWILIO_PHONE,
        to=SEND_TO_PHONE
    )
    print(message.status)

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
