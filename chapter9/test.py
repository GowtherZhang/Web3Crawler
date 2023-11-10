import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
response = requests.get(url='https://m.bqg20.cc/list/12769/1183.html', headers=headers,proxies={''}).text
with open('ip.html', 'w', encoding='utf-8') as fp:
    fp.write(response)