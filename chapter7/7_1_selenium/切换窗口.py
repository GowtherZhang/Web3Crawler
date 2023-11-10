from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get(url='https://www.baidu.com')
print(browser.window_handles)
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get(url='https://www.jd.com')
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])
browser.get(url='https://python.org')
