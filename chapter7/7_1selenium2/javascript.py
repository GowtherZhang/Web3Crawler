from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_experimental_option('detach', True)
option.add_argument('--start-maximized')

# url = 'https://www.zhihu.com/explore'
# browser = webdriver.Chrome(options=option)
# browser.get(url=url)

# 定位节点
# square = browser.find_element(By.ID, 'guestSquare')

# 输出text
# title_1 = browser.find_element(By.XPATH, '//div[@class="css-1g4zjtl"]/a[1]')
# print(title_1.text)

# 获取 ID、位置、标签名、大小
# input = browser.find_element(By.XPATH, '//input[@id="Popover1-toggle"]')
# print(input.text)
# print(input.tag_name)
# print(input.id)
# print(input.location)
# print(input.size)

# # 切换Frame
# from selenium.common.exceptions import NoSuchElementException
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# try:
#     drop = browser.find_element(By.ID, "droppable")
# except NoSuchElementException:
#     print("No such element")

# #切换为子frame
# browser.switch_to.frame('iframeResult')
# drag = browser.find_element(By.ID, 'draggable')
# print(drag.text)
# #切换为父frame
# browser.switch_to.parent_frame()
# try:
#     drag = browser.find_element(By.ID, 'draggable')
#     print(drag.text)
# except NoSuchElementException:
#     print("No such element!")

# 隐式等待与显示等待
# url = 'https://jd.com'
# browser = webdriver.Chrome(options=option)
# browser.get(url)
# browser.implicitly_wait(10) # 隐式等待
# browser.get(url=url)
# input = browser.find_element(By.ID, 'key')
# print(input.tag_name)

# from  selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# wait = WebDriverWait(browser, 10) #如果10秒内加载出来，就返回该节点，如果10秒内没有加载出来，则返回异常
# input = wait.until(EC.presence_of_element_located((By.ID, 'key')))
# button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button"]')))
# print(input, button)

#前进后退
# browser = webdriver.Chrome(options=option)
# browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# time.sleep(5)
# browser.get('https://jd.com')
# time.sleep(5)
# button = browser.find_element(By.XPATH, '//button[@class="button"]')
# button.click()
# time.sleep(5)
# browser.back()
# browser.forward()
# browser.get('https://www.zhihu.com/explore')

#cookies
# browser = webdriver.Chrome(options=option)
# browser.get('https://www.zhihu.com/explore')
# cookies = browser.get_cookies()
# print(cookies)
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# cookies2 = browser.get_cookies()
# print(cookies2)
# browser.delete_all_cookies()
# cookies3 = browser.get_cookies()
# print(cookies3  )

#选项卡操作
