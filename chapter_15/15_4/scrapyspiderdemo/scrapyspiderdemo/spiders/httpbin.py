import scrapy
from scrapy import Request
# from scrapy.http import JsonRequest, FormRequest

class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["www.httpbin.org"]
    start_url = "https://www.httpbin.org/get"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    # data = {'name':'germey','age':'26'}
    cookies = {'name':'germey','age':'26'}

    def start_requests(self):
        for offset in range(5):
            url = self.start_url + f'?offset = {offset}'
            yield Request(url, headers=self.headers,
                          cookies=self.cookies,
                          callback=self.parse_response,
                          meta={'offset':offset})

    # def start_requests(self):
    #     yield FormRequest(self.start_url,
    #                     callback = self.parse_response,
    #                     formdata=self.data)
    #     yield JsonRequest(self.start_url,
    #                     callback=self.parse_response,
    #                     data=self.data)


    def parse_response(self, response):
        # print('url', response.url)
        # print('request', response.request)
        # print('status',response.status)
        print('headers',response.headers)
        # print('text',response.text)
        # print('meta',response.meta)
        # print('request',response.request)
        # print('ip',response.ip_address)