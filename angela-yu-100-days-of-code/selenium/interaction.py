from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ua = UserAgent()
user_agent = ua.random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"user-agent={user_agent}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

# Find "Content portals" link by text and click it
all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# Fill in search box and hit ENTER
search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.RETURN)

# driver.quit()
