import requests

requests.get('https://www.httpbin.org/cookies/set/number/123456789')
r = requests.get('http://www.httpbin.org/cookies')
print(r.text)