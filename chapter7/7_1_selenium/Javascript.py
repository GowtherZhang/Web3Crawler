from selenium import webdriver

browser = webdriver.Chrome()
browser.get(url='https://www.jd.com/')
browser.maximize_window()
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("to Bottom")')

# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')