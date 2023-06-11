from bs4 import BeautifulSoup
import requests
import smtplib
from PRIVATE.my_email import MyEmail

URL = "https://www.amazon.com/10-Frames-Complete-Beehive-Beeswax-Foundation/dp/B082DJGWXL/ref=sr_1_5?crid=3A6PTWZ3BH0RI&keywords=bee+hive&qid=1686451659&sprefix=bee+hi%2Caps%2C212&sr=8-5&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0"

# NOTE: Amazon does NOT allow web scraping via bots. In order to bypass this and
#       get the desired response, use these headers. This will esentially trick
#       Amazon into thinking the request is coming from a browser. Please do NOT
#       abuse this work-around. Always follow a website's code of ethics. If you
#       want more info on a particular website's automated bot policies, go to:
#
#       '[example-website.com]/robots.txt'
#
#       Thanks :)

HEADERS = {
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0)' 'Gecko/20100101' 'Firefox/114.0'),
    'Accept-Language': 'en-US, en;q=0.5'
}

my_email = MyEmail().email_addr
my_smtp = MyEmail().smtp
my_passwd = MyEmail().password
send_to_addr = MyEmail().send_to_addr

response = requests.get(url=URL, headers=HEADERS)
content = response.text
soup = BeautifulSoup(content, "html.parser")

price_tag = soup.select_one(selector=".a-price-whole")
price = int(price_tag.getText().split(".")[0])

if price <= 150:
    with smtplib.SMTP(my_smtp, port=587) as connection:
        # Make connection secure
        connection.starttls()
        # Log in
        connection.login(user=my_email, password=my_passwd)
        # Send mail
        connection.sendmail(
            from_addr=my_email,
            to_addrs=send_to_addr,
            msg=f"Subject: Bee Hive Price Alert!\n\nThe Bee Hive you are interested in has dropped below your target price. Here's the link to the product:\n\n{URL}")
