# http 代理服务
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener

# proxy = '36.138.56.214:3128'
# proxyhandler = ProxyHandler({
#     'http':'http://' + proxy,
#     'https':'https://' + proxy
# })

# opener = build_opener(proxyhandler)
# try:
#     response = opener.open('http://httpbin.org/get')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

#socks5类型
# import socks
# import socket
# from urllib.error import URLError
# from urllib import request

# socks.setdefaultproxy(socks.SOCKS5, '36.138.56.214', 3128)
# socket.socket = socks.socksocket
# try:
#     response = request.urlopen('http://httpbin.org/get')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

# 使用requests
# import requests

# proxy = '36.138.56.214:3128'
# proxies = {
#     'http':'http://' + proxy,
#     'https':'https://' + proxy
# }
# url = 'http://httpbin.org/get'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# }
# try:
#     response = requests.get(url=url, headers=headers, proxies=proxies)
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print('Error', e.args)

# 使用Selenium
from selenium import webdriver

proxy = '36.138.56.214:3128'
options = webdriver.ChromeOptions()
options.add_argument('--proxy-sever=http://'+proxy)
options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_experimental_option('detach',True)
options.add_argument('--start-maximized')

browser = webdriver.Chrome(chrome_options=options)
browser.get('http://httpbin.org/get')
print(browser.page_source)