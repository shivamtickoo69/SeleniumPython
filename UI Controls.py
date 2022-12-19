from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(1)
CheckBoxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(CheckBoxes))
for CheckBox in CheckBoxes:
    if CheckBox.get_attribute("value") == "option3":
        CheckBox.click()
        break
        
time.sleep(2)

#RADIO BUTTON
RadioButtons = driver.find_elements(By.CSS_SELECTOR, "input[class = 'radioButton']")
RadioButtons[2].click()
time.sleep(2)
assert RadioButtons[2].is_selected

#Hide Box code

assert driver.find_element(By.XPATH, "//input[@placeholder = 'Hide/Show Example']").is_displayed
driver.find_element(By.CSS_SELECTOR, "input[onclick = 'hideElement()']").click()
time.sleep(2)
#assert not driver.find_element(By.XPATH, "//input[@placeholder = 'Hide/Show Example']").is_displayed
name = "shivam"

driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "confirmbtn").click()
time.sleep(2)
Alert = driver.switch_to.alert
AlertText = Alert.text
time.sleep(2)
print(AlertText)
assert name in AlertText
Alert.accept()


