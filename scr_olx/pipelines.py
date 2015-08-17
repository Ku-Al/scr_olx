# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import signals
import json
import codecs


class ScrOlxPipeline(object):
    def __init__(self):
        self.file = open('ScrOlx.json', 'wb')

    def process_item(self, item, spider):
        try:
            line = json.dumps(dict(item), ensure_ascii=True, sort_keys=True, indent=4) + "\n"
        except UnicodeEncodeError:
            print dict(item) + " \n"

        self.file.write(line)
        return item
    
    def spider_closed(self, spider):
        self.file.close()

