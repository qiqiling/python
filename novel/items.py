# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    img = scrapy.Field()
    author=scrapy.Field()
    uptx=scrapy.Field()
    descr=scrapy.Field()
    source=scrapy.Field()