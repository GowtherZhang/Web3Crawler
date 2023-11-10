import requests
from requests.auth import HTTPBasicAuth

r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
print(r.status_code)
print(r.text[:200])