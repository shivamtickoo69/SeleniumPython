from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
time.sleep(2)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am the best")
driver.switch_to.default_content()
out = driver.find_element(By.CSS_SELECTOR,"h3").text
print(out)
time.sleep(2)



