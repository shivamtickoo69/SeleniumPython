from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
time.sleep(1)
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
Country = driver.find_elements(By.XPATH, "//li[@class = 'ui-menu-item']/a")
print(len(Country))

for c in Country:
    if c.text == "India":
        c.click()
        break

time.sleep(5)
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"


