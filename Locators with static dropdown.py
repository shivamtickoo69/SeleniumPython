from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Shivam")
driver.find_element(By.NAME,"email").send_keys("shivamtickoo82@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("shivamtickoo82@gmail.com")
driver.find_element(By.ID,"exampleCheck1").click()
# Now we will start static dropdown here
Select = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
Select.select_by_visible_text("Female")
Select.select_by_index(1)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR,"input[id='inlineRadio2']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
time.sleep(17)