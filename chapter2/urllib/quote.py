from urllib.parse import quote

keyword = '壁纸'
url = 'https://baidu.com/s?wd=' + quote(keyword)
print(url)