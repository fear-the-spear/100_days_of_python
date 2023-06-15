from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

AMZN_URL = "https://www.amazon.com/10-Frames-Complete-Beehive-Beeswax-Foundation/dp/B082DJGWXL/ref=sr_1_6?crid=1YQ6QIPRFHKL1&keywords=bee+hive&qid=1686501923&sprefix=bee+hiv%2Caps%2C241&sr=8-6&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0"
PYTHN_URL = "https://www.python.org"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# AMAZON URL ###################################################################
# driver.get(AMZN_URL)
# price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
# print(price.text)

# PYTHON URL ###################################################################
driver.get(PYTHN_URL)
search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("class"))
logo = driver.find_element(By.CLASS_NAME, "python-logo")
print(logo.size)
doc_link = driver.find_element(By.CSS_SELECTOR, "div.documentation-widget a")
print(doc_link.text)
stories_link = driver.find_element(
    By.XPATH, '/html/body/div/footer/div[1]/div/ul/li[4]/ul/li[13]/a')
print(stories_link.text)
all_divs = driver.find_elements(By.TAG_NAME, "div")
print(all_divs[0].text)

# upcoming events challenge ####################################################
time_tags = driver.find_elements(By.CSS_SELECTOR, "div.last ul li time")
# times = [tags.text for tags in time_tags] <- unnecessary line of code

event_tags = driver.find_elements(By.CSS_SELECTOR, "div.last ul li a")
# events = [tags.text for tags in event_tags] <- unnecessary line of code

dictionary = {
    n: {"time": time_tags[n].text, "name": event_tags[n].text} for n in range(5)
}

print(dictionary)
# driver.close()
driver.quit()
