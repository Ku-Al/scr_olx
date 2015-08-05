# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ScrOlxItem(Item):
    # define the fields for your item here like:
    # name = Field()
    id = Field()
    adv_title = Field()
    url = Field()
    adress = Field()
    data = Field()
    advertisement = Field()

