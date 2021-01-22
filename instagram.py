from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://www.facebook.com")

time.sleep(3)
driver.find_element_by_id("email").send_keys("vd101010")
time.sleep(3)
driver.find_element_by_id("pass").send_keys("1233445465656")
time.sleep(3)
driver.find_element_by_name("login").click()
