from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
Cart = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")
count  = len(Cart)
assert count > 0
time.sleep(2)

#Chaining method in selenium
#driver.find_element(By.XPATH, "//div[@class = 'products']/div/div/button").click()
for result in Cart:
    result.find_element(By.XPATH, "div/button").click()

time.sleep(2)

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text() ='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
time.sleep(2)
