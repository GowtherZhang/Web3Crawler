from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-logging'])
option.add_experimental_option('detach', True)
option.add_argument('--start-maximized')

browser = webdriver.Chrome(options=option)
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)

browser.switch_to.frame('iframeResult')
source = browser.find_element(By.XPATH, '//div[@id="draggable"]')
target = browser.find_element(By.XPATH, '//div[@id="droppable"]')

action = ActionChains(browser)
action.drag_and_drop(source, target)
action.perform()