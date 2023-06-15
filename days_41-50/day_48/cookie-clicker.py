from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

COOKIE_URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)

browser.get(COOKIE_URL)

is_on = True


def click_cookie():
    cookie = browser.find_element(By.ID, "cookie")
    timeout = 5
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        cookie.click()


def upgrade():
    store = browser.find_elements(By.CSS_SELECTOR, "div#store div")
    for item in store[::-1]:
        if item.get_attribute("class") == "":
            item.click()
            break


while is_on:
    t = 300
    t_start = time.time()
    while time.time() < t_start + t:
        click_cookie()
        upgrade()
    is_on = False

total_cookies = browser.find_element(By.CSS_SELECTOR, "div#money")
cookies_per_sec = browser.find_element(By.CSS_SELECTOR, "div#cps")
print(f"Cookies Clicked Per Second: {cookies_per_sec.text.split(' ')[-1]}")
