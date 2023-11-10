from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.get(url='https://www.baidu.com')
except TimeoutException:
    print('Time out')
try:
    browser.find_element(by=By.ID, value='hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()