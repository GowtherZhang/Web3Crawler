import requests
import logging

logging.captureWarnings(True)
response = requests.get('https://ssr2.scrape.center/', verify=False)
print(response.status_code)