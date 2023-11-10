from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) #禁用DevTools on ws。。。
options.add_experimental_option('detach', True)  #不自动关闭浏览器
options.add_argument('--start-maximized')#浏览器窗口最大化
browser = webdriver.Chrome(options=options)

# print(browser.page_source)
input_first = browser.find_element(By.ID, 'key')
input_second = browser.find_element(By.XPATH, '//input[@id="key"]')

input_second.send_keys('ipad')
input_second.clear()
input_second.send_keys('体温计')

button = browser.find_element(By.XPATH, '//button[@class="button"]')
button.click()

# print(input_first, "\n", input_second)
# browser.close()