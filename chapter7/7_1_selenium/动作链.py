from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get(url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')
source = browser.find_element(by=By.CSS_SELECTOR, value='#draggable')
Target = browser.find_element(by=By.CSS_SELECTOR, value='#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, Target)
actions.perform()