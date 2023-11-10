import scrapy


class BernardiSpider(scrapy.Spider):
    name = "bernardi"
    allowed_domains = ["acura.bernardiparts.com"]
    start_urls = ["https://acura.bernardiparts.com"]

    def parse(self, response):
        pass
