from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_id("email").send_keys("vd101010")
time.sleep(3)
driver.find_element_by_id("pass").send_keys("dummy")
time.sleep(3)
driver.find_element_by_name("login").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id=\"mount_0_0\"]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/label/input").send_keys("@useinsider")
time.sleep(4)
driver.find_element_by_xpath("//*[@id=\"mount_0_0\"]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/label/input").send_keys(Keys.ENTER)
time.sleep(5)
driver.find_elements_by_css_selector("#mount_0_0 > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.jifvfom9.gs1a9yip.owycx6da.btwxx1t3.buofh1pr.dp1hu0rb.ka73uehy > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.dp1hu0rb > div > div > div > div > div > div > div:nth-child(1) > div > div > div > div > div > div > div.ozuftl9m.taijpn5t.cbu4d94t.j83agx80 > div").click()