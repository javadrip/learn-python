from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

# Randomizes user agent to avoid detection
ua = UserAgent()
user_agent = ua.random

# Keeps Chrome browser open after program ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
print(f"Price: ${price_dollar}.{price_cents}")

# driver.close()
# driver.quit()
