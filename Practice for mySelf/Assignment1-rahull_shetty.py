from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import time
import re
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
time.sleep(3)
WindowsOpened = driver.window_handles
driver.switch_to.window(WindowsOpened[1])
Text = (driver.find_element(By.CSS_SELECTOR,".im-para.red")).text
Trim = Text.split('at')
parsed_text = Trim[1].strip()
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
email = re.search(email_pattern, parsed_text).group()
print(email)
#Trim = Text.lstrip("mentor@rahulshettyacademy.com")
#Trim = Text.split('at', 'with')
time.sleep(2)
