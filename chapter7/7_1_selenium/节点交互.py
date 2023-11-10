from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get(url='https://www.jd.com/')
input = browser.find_element(by=By.ID, value='key')
input.send_keys('毛绒玩具')
time.sleep(3)
input.clear()
input.send_keys('男裤')
button = browser.find_element(by=By.CLASS_NAME, value='button')
button.click()
time.sleep(3)
print(browser.current_url)
browser.close()