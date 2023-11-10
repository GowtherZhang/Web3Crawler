from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get(url='https://www.zhihu.com/explore')
for title in browser.find_elements(by=By.CSS_SELECTOR, value='.css-1nd7dqm'):
    print(title.text)