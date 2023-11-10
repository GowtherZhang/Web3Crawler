#隐式等待
from selenium import webdriver
from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get(url='https://www.zhihu.com/explore')
# browser.implicitly_wait(10)
# input = browser.find_element(by=By.CSS_SELECTOR, value='.Input')
# print(input)
# print(type(input))
# browser.close()

#显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.get(url='https://www.jd.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'text')))
button =wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button')))
print(input)
print(button)
browser.close()