import scrapy


class QuotersSpider(scrapy.Spider):
    name = 'quoters'
    allowed_domains = ['quotes.com']
    start_urls = ['http://quotes.com/']

    def parse(self, response):
        pass
