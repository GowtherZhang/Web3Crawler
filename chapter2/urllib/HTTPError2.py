import socket
from urllib import request, error

try:
    response = request.urlopen('https://baidu.com', timeout=0.01)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')