from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By

# Randomizes user agent to avoid detection
ua = UserAgent()
user_agent = ua.random

# Keeps Chrome browser open after program ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"user-agent={user_agent}")

driver = webdriver.Chrome(options=chrome_options)
# driver.get(
#     "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# )

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"Price: ${price_dollar}.{price_cents}")


driver.get("https://www.python.org/")

# Search for events
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for time in event_times:
#     print(time.text)
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# for name in event_names:
#     print(name.text)
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.close()
# driver.quit()
