# Challenge 1: Email A Motivational Quote To Yourself If Date = Monday
# NOTE: For testing, check if weekday = today so there's no waiting
import datetime as dt
import smtplib
import random
from PRIVATE.email_data import MyEmail

my_email = MyEmail().email_addr
my_smtp = MyEmail().smtp
my_passwd = MyEmail().password
send_to_addr = MyEmail().send_to_addr

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:
    with open("quotes.txt", "r") as quotes:
        q_list = quotes.readlines()
        random_quote = random.choice(q_list)

    with smtplib.SMTP(my_smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_passwd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=send_to_addr,
            msg=f"Subject: Your Weekly Motivational Quote!\n\n{random_quote}")
