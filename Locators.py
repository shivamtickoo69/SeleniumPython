from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Shivam")
driver.find_element(By.NAME,"email").send_keys("shivamtickoo82@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("shivamtickoo82@gmail.com")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR,"input[id='inlineRadio2']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
# For Xpath //tagname[@attribute='value']
# For CSS selector  tagname[attribite= 'value'] #id, .ClassName 
# If there are 3 box so for that we  have to enter for CSS selector : (tagname[attribute= 'Value'])[5]
time.sleep(12)
assert "success" in message

