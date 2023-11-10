from scrapy import Request, Spider
import scrapy


class HttpbinSpider(Spider):
    name = "httpbin"
    allowed_domains = ["www.httpbin.org"]
    start_url = "https://www.httpbin.org/get"
    

    def start_requests(self):
        for offset in range(5):
            url = f'{self.start_url}?query = {offset}'
            yield Request(url, callback=self.parse)


    def parse(self, response):
        item = DemoItem(**response.json())
        yield item
        print('status', response.status)


class DemoItem(scrapy.Item):
    origin = scrapy.Field()
    headers = scrapy.Field()
    args = scrapy.Field()
    url = scrapy.Field()
