from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-logging']) # 禁用DevTools on ws
option.add_experimental_option('detach', True) # 不自动关闭浏览器
option.add_argument('--start-maximized') # 浏览器窗口最大化


browser = webdriver.Chrome(options=option)
browser.get('https://jd.com')
input_first = browser.find_element(By.XPATH, '//input[@id="key"]')
input_first.send_keys("红米至尊K30")
time.sleep(5)
input_first.clear()
time.sleep(5)

input_second = browser.find_element(By.ID, 'key')
input_second.send_keys('小米12')

button = browser.find_element(By.XPATH, "//button[@class='button']")
button.click()