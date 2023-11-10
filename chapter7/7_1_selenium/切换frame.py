from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
browser.get(url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element(by=By.CLASS_NAME, value='logo')
except NoSuchElementException:
    print('NO LOGO')

browser.switch_to.parent_frame()

try:
    logo2 = browser.find_element(by=By.CLASS_NAME, value='logo')
    print(logo2)
    print(logo2.text)
    print(logo2.get_attribute(name='class'))
except NoSuchElementException:
    print('No logo')
browser.close()