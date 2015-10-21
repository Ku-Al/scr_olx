import re
import json
from urlparse import urlparse
import urllib

from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from scr_olx.items import *
#from misc.log import *
#from misc.spider import CommonSpider
 

#from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#from src_olx.items import ScrOlxItem 

#from scrapy.loader.processor import TakeFirst
#from scrapy.loader import XPathItemLoader
#from scrapy.selector import HtmlXPathSelector
#from orphanage.items import OrphanageItem


class OlxSpider(CrawlSpider):
    name = "scr_olx"
    allowed_domains = ['odessa.od.olx.ua']
    start_urls = ['http://odessa.od.olx.ua/nedvizhimost/arenda-kvartir/dolgosrochnaya-arenda-kvartir/']

    rules = [
        # The first rule to follow a link from this page - follow=True
        #Rule(LinkExtractor(allow=('?page=', )), follow=True),
        # Second rule for the pages on which we extract information
#        Rule(LinkExtractor(allow='[0-5]',), callback='parse_item')
        Rule(LinkExtractor(allow='\?page=[1-5]',), callback='parse_item')
    ]

    def parse_item(self, response):

#        items = []   
        item = ScrOlxItem()

        item['url'] = response.xpath('//h3[@class="x-large lheight20 margintop5"]/a/@href').extract()
        item['title'] = response.xpath('//h3[@class="x-large lheight20 margintop5"]/a/strong/text()').extract()
        item['data'] = response.xpath('//p[@class="color-9 lheight16 marginbott5 x-normal"]/text()').extract()
        item['cost'] = response.xpath('//p[@class="price"]/strong/text()').extract()
#        items.append(item) 
#        print items    
        return item
