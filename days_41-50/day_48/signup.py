# NOTE: can't do this exercise because the form now contains captcha and
#   we haven't yet been taught how to deal with that

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# import time

# SIGNUP_URL = "https://londonappbrewery.com/sendy/subscription?f=m7Xj2bDOCQnlJ27yezLEAtJi1mhUIxOaJcJGZYMLLX6wx5MZd0b2FunBI8dOomNt"

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(options=chrome_options)

# browser.get(SIGNUP_URL)

# name_input = browser.find_element(By.CSS_SELECTOR, "input[id='name']")
# name_input.send_keys("Dakota Bowman")
# email_input = browser.find_element(By.CSS_SELECTOR, "input[id='email']")
# email_input.send_keys("py.stuff@yahoo.com")
# checkbox = browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
# checkbox.click()
# captcha = browser.find_element(By.CSS_SELECTOR, "span[id='recaptcha-anchor']")
# print(captcha.location)
# # submit = browser.find_element(By.CSS_SELECTOR, "a[id='submit']")
# # submit.click()

# # time.sleep(2)
