import scrapy 

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from items.scr_olx import ScrOlxItem 

#from scrapy.loader.processor import TakeFirst
#from scrapy.loader import XPathItemLoader
#from scrapy.selector import HtmlXPathSelector
#from orphanage.items import OrphanageItem


class OlxSpider(CrawlSpider):
    name = "scr_olx"
    allowed_domains = ['odessa.od.olx.ua']
    #start_urls = ['http://odessa.od.olx.ua/nedvizhimost/arenda-domov/dolgosrochnaya-arenda-domov/']
    start_urls = ['http://odessa.od.olx.ua/nedvizhimost/arenda-domov/dolgosrochnaya-arenda-domov/']

    rules = [
        # The first rule to follow a link from this page - follow=True
        #Rule(LinkExtractor(allow=('?page=', )), follow=True),
        # Second rule for the pages on which we extract information
        Rule(LinkExtractor(allow=['\d+', ]), callback='parse_item')
    ]

    def parse_item(self, response):
        self.log('-------------Start parser from %s' % response.url)
#        hxs = HtmlXPathSelector(response)
#        l = OrphanLoader(OrphanageItem(), hxs)
#        l.add_xpath('url', "//h3[@class='large lheight20 margintop10']/a[@href]" % u"URL:")
#        l.add_xpath('url', "//h3[@class='x-large lheight20 margintop5']/a[@href]" % u"URL:")
#        l.add_xpath('title', "//h3[@class='x-large lheight20 margintop5']/a[@href]/span" % u"Title:")
#        l.add_value('data', response.url)
#        return l.load_item()
        item = ScrOlxItem()
        item['url'] = response.xpath('//h3[@class="x-large lheight20 margintop5"]/a[@href]').extract()
        item['title'] = response.xpath('//h3[@class="x-large lheight20 margintop5"]/a[@href]/span').extract()
        return item
