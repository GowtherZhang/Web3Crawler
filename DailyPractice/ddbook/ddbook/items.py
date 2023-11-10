# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DdbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    introduction = scrapy.Field()
    price = scrapy.Field()
    press = scrapy.Field()
    time = scrapy.Field()
    comment_num = scrapy.Field() 