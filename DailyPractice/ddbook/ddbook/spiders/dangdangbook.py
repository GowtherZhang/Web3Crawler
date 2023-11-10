import scrapy
from ..items import DdbookItem 


class DangdangbookSpider(scrapy.Spider):
    name = "dangdangbook"
    allowed_domains = ["www.dangdang.com"]
    start_urls = ['http://search.dangdang.com/?key=python']
    PageNum = 3

    def parse(self, response):
        books = response.xpath('//ul[@class="bigimg"]/li')
        for book in books:
            item = DdbookItem()
            item['name'] = book.xpath('//a[@class="pic"]/@title').extract()
            item['author'] = book.xpath('//p[@class="search_book_author"]//a[@name="itemlist-author"]/text()').extract() if len( book.xpath('//p[@class="search_book_author"]//a[@name="itemlist-author"]/text()'))>0 else '无作者信息'
            item['introduction'] = book.xpath('//p[@class="detail"]/text()').extract() if len(book.xpath('//p[@class="detail"]/text()').extract()) > 0 else '无介绍信息'
            item['price'] = book.xpath('//p[@class="price"]/span/text()').extract()
            item['press'] = book.xpath('//p[@class="search_book_author"]//a[@name="P_cbs"]/text()').extract() if len(book.xpath('//p[@class="search_book_author"]//a[@name="P_cbs"]/text()')) > 0 else '无出版社信息'
            item['time'] = book.xpath('//p[@class="search_book_author"]/span[2]/text()').extract() if len(book.xpath('//p[@class="search_book_author"]/span[2]/text()')) else '无出版时间信息'
            item['comment_num'] = book.xpath('//p[@class="search_star_line"]/a/text()').extract()
            yield item

    def start_requests(self):
        for page in range(2, self.PageNum+1):
            url = f'{self.start_urls[0]}&page_index={page}'
            yield scrapy.Request(url, callback=self.parse)