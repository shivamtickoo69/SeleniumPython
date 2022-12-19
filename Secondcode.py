from selenium import webdriver
from selenium.webdriver.chrome.service import Service
Service_obj = Service("C:\\Users\\SHIVAM\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.chrome(Service = Service_obj)
driver.get("https://www.google.com/pq/")