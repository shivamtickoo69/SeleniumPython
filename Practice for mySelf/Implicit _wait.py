from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
cart = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")
count = len(cart)
assert count > 0

for result in cart:
    result.find_element(By.XPATH,"div/button").click()

time.sleep(2)
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
Wait  = WebDriverWait(driver, 10)
Wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)






