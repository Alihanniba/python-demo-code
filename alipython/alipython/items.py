# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.Item import Item,Field


class AlipythonItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    name = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    img = scrapy.Field()
