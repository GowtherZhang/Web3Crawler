# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class ScrapyitempiplinedemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MovieItem(Item):
    name = Field()
    categories = Field()
    score = Field()
    drama = Field()
    directors = Field()
    actors = Field()
