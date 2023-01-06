# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

# def remove_currency(value):
#     return value.replace('£','').strip()


# class FirstprojectItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     price=scrapy.Field(input_processor=MapCompose(remove_tags,remove_currency),output_processor=TakeFirst())
#     image=scrapy.Field(input_processor=MapCompose(remove_tags),output_processor=TakeFirst())
    
#     link=scrapy.Field()





class FirstprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price=scrapy.Field()
    image=scrapy.Field()
    link=scrapy.Field()
    category_name=scrapy.Field()
    title_name=scrapy.Field()
    
