from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(2)
WindowsOpened = driver.window_handles
driver.switch_to.window(WindowsOpened[1])
print(driver.find_element(By.TAG_NAME,'h3').text)
driver.close()
driver.switch_to.window(WindowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3")
time.sleep(2)
