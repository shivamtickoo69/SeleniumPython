from selenium.webdriver.chrome import webdriver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://magento.softwaretestingboard.com/")
driver.find_element(By.LINK_TEXT,"Create an Account").click()
driver.find_element(By.ID,"firstname").send_keys("Shivam")
driver.find_element(By.ID, "lastname").send_keys("Tickoo")
driver.find_element(By.CSS_SELECTOR,".checkbox").click()
driver.find_element(By.NAME,"email").send_keys("Tickoo1@example.com")
Old =driver.find_element(By.ID,"password").send_keys("Tickoo@123")
conf = driver.find_element(By.CSS_SELECTOR,'#password-confirmation').send_keys("Tickoo@1423")
if Old == conf:
    driver.find_element(By.CSS_SELECTOR,".action.submit.primary").click()

time.sleep(5)