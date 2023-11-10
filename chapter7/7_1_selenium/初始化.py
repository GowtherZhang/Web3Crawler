from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get(url='https://taobao.com')
# input_first = browser.find_element_by_id('q')
input_first = browser.find_element(by=By.ID, value='q')
# input_second = browser.find_element_by_name('q')
input_second = browser.find_element(by=By.NAME, value='q')
# input_third = browser.find_element_by_css_selector('#q')
input_third = browser.find_element(by=By.CSS_SELECTOR, value='#q')
# input_forth = browser.find_element_by_xpath('//*[@id="q"]')
input_forth= browser.find_element(by=By.XPATH, value='//*[@id="q"]')
# input.send_keys('靠枕')
# input.send_keys(Keys.ENTER)


# print(browser.page_source)
print(input_first)
print(input_second)
print(input_third)
print(input_forth)
browser.close()