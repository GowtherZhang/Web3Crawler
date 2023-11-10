import requests

url = 'https://spa1.scrape.center/page/1'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

response = requests.get(url,headers=headers).text
print(response)