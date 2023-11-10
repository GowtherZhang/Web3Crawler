import requests

s = requests.session()
s.get('https://www.httpbin.org/cookies/set/number/123456789')
r = s.get('http://www.httpbin.org/cookies')
print(r.text)