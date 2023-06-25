# Data Entry Automation

# imports
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import time

# constants
DOCS_URL = "https://forms.gle/VSBRy7jTVGqBW4bs7"
ZILLOW_URL = f"https://www.zillow.com/columbus-oh/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A40.157272%2C%22east%22%3A-82.786297%2C%22south%22%3A39.808631%2C%22west%22%3A-83.189959%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A10920%2C%22regionType%22%3A6%7D%5D%7D"
HEADERS = {
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0)' 'Gecko/20100101' 'Firefox/114.0'),
    'Accept-Language': 'en-US, en;q=0.5'
}

# selenium options setup
options = Options()
options.add_experimental_option("detach", True)

# get response in html from zillow url and turn to soup
zillow = requests.get(url=ZILLOW_URL, headers=HEADERS)
content = zillow.text
soup = BeautifulSoup(content, "html.parser")

# get list of all rental listing 'cards'
listings = soup.select(selector="ul.photo-cards")

# pull address data from cards
addr_elements = [item.find_all(name="address", limit=30) for item in listings]
addrs = [item.text for item in addr_elements[0]]

# pull price data from cards
price_elements = [item.select(
    selector="span[data-test='property-card-price']") for item in listings]
prices = [item.text for item in price_elements[0]]

# pull links to rental listings from cards
listing_links = [item.select(
    selector="a[tabindex='0']") for item in listings]
links = [item.get("href") for item in listing_links[0]]

# open browser with selenium
browser = webdriver.Chrome(options=options)

for n in range(9):
    browser.get(DOCS_URL)
    time.sleep(2)
    addr_input = browser.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    addr_input.click()
    addr_input.send_keys(addrs[n])
    price_input = browser.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input.click()
    price_input.send_keys(prices[n])
    link_input = browser.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input.click()
    link_input.send_keys(links[n])
    time.sleep(1)
    submit_btn = browser.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    submit_btn.click()
    # submit_another_res = browser.find_element(
    #     By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    # submit_another_res.click()

# NOTE: Google no longer allows selenium to log into your google account
# for you. Because of this, the last step of the project - creating a Google
# sheet out of the submitted forms - cannot be done. So, this project includes
# everything except that last step. Once I ran the code, I just opened a
# browser window and created a Google sheet manually.
