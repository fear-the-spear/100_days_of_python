import time
import smtplib
import requests
from datetime import datetime
from PRIVATE.email_data import MyEmail

URL = "https://api.sunrise-sunset.org/json"
MY_LAT = float("40.869331")
MY_LNG = float("-82.317917")

my_email = MyEmail().email_addr
my_smtp = MyEmail().smtp
my_passwd = MyEmail().password
send_to_addr = MyEmail().send_to_addr


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()["iss_position"]

    iss_lng = float(iss_data["longitude"])
    iss_lat = float(iss_data["latitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG + 5:
        return True


def is_night():
    params = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    sun_response = requests.get(URL, params=params)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


# If you run this program, it will stay running in the background and
#   check every x minutes if the iss is close overhead. If you don't want
#   the program to constantly run in the background, take the following
#   code out of the while loop and remove 'time.sleep(60)' and it will just
#   run once 😉
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(
            user=my_email,
            password=my_passwd
        )
        connection.sendmail(
            from_addr=my_email,
            to_addrs=send_to_addr,
            msg="Subject: Look UP☝🏼\n\nThe ISS is overhead!"
        )
