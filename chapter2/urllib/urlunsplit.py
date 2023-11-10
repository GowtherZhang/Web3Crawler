from urllib.parse import urlunsplit

data = ['https', 'www.baidu.com', 'index.html;user', 'id=5', 'comment']
print(urlunsplit(data))