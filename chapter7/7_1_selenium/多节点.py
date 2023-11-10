from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get(url='https://www.taobao.com/')
tags=[]
for element in browser.find_elements(by=By.CSS_SELECTOR, value='.service-bd li a'):
    tags.append(element)
print(tags)