# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#

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

