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
driver.get(
    "https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/"
)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("John")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Smith")

email = driver.find_element(By.NAME, "email")
email.send_keys("abc@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
