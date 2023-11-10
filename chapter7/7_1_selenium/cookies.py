from selenium import webdriver

browser = webdriver.Chrome()
browser.get(url='https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name':'name', 'domain':'www.zhihu.com', 'value':'germey'})
print(browser.get_cookie)
browser.delete_all_cookies()
print(browser.get_cookies())