from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/index.htm")
time.sleep(2)
#url ="register.htm"
#driver.get("register.htm")
driver.find_element(By.LINK_TEXT("Register")).click()
time.sleep(5)
