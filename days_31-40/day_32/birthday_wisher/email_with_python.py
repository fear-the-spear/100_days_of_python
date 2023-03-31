import smtplib
from PRIVATE.email_data import MyEmail

# I've set up a class with variables containing my personal data
#   so I don't expose my personal data publicly.
my_email = MyEmail().email_addr
my_smtp = MyEmail().smtp
my_passwd = MyEmail().password
send_to_addr = MyEmail().send_to_addr

# Set up connection
with smtplib.SMTP(my_smtp, port=587) as connection:
    # Make connection secure
    connection.starttls()
    # Log in
    connection.login(user=my_email, password=my_passwd)
    # Send mail
    connection.sendmail(
        from_addr=my_email,
        to_addrs=send_to_addr,
        msg="Subject: Hello!\n\nThis is the body of the email.")

# If 'with' keyword is not used, we must close the connection:
# connection.close()
