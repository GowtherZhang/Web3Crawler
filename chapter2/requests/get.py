import requests

data = {
    'name':'germey',
    'age': 24
}
r = requests.get('https://www.httpbin.org/get',params=data)
print(type(r.text))
print(r.text)
print(type(r.json()))
print(r.json())