import requests
from twilio.rest import Client
from PRIVATE.private import *

# NOTE:
# 1. You will have to create your own variables with
#    values assigned to you when creating accounts for
#    both API's used in this project for this app to work.
#
# 2. I recommend creating a 'private.py' file inside a
#    'PRIVATE' directory so you can use line 2 as is.
#    E.G. ./PRIVATE/private.py
#
# 3. APIs Used: Open Weather Map, Twilio
#
# 4. The variable names I used are as follows:
#    lat (latitude)
#    lng (longitude)
#    default (Open Weather Map API Token)
#    OWM_Endpoint (Open Weather Map API Endpoint)
#    account_sid (Twilio API Id)
#    auth_token (Twilio API auth token)
#    uhyota (Personal Phone Number)
#    falcon (Personal Phone Number)
#    twilio_phone_num (twilio-assigned number used to send sms)

params = {
    "lat": lat,
    "lon": lng,
    "units": "imperial",
    "exclude": "current,minutely,daily",
    "appid": default
}

response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()
code = response.status_code
weather_data = response.json()["hourly"]
weather_slice = weather_data[:12]

# Make list of all weather codes for the next 12 hours
weather_codes = [hour["weather"][0]["id"] for hour in weather_slice]

# Check all itmes in 'weather_codes'. If any of them is under 700,
#   change 'will_rain' var to True and send SMS that tells recipient
#   to bring an umbrella.
will_rain = False
for code in weather_codes:
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        from_=twilio_phone_num,
        to=uhyota
    )

    print(message.status)
