import requests

proxies = {
    'http': 'http://user:password@10.10.10.10:1080',
    'https': 'https://user:password@10.10.10.10:1080'
}
requests.get('https:/www.httpbin.org/get', proxies=proxies)
