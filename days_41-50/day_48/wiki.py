from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

WIKI_URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)

browser.get(WIKI_URL)

# challenge 1 - print the article count to the console
en_articles = browser.find_element(
    By.CSS_SELECTOR, "a[title='Special:Statistics']")
print(en_articles.text)

# click on an element
# en_articles.click()
# all_portals = browser.find_element(By.LINK_TEXT, "anyone can edit")
# all_portals.click()

# use an input (search bar)
search = browser.find_element(By.ID, "searchInput")
search.send_keys("Python", Keys.ENTER)

time.sleep(2)
browser.close()
