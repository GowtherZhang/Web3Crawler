from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/404/11111')
    print(response.read().decode('utf-8'))
except error.URLError as e:
    print(e.reason)