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
         self.file = codecs.open('olx_home.html', 'w', encoding='utf-8')
         self.file.write(u'<html lang="ru-RU">\n')
         self.file.write(u'<head>\n')
         self.file.write(u'<title>Grab наOlx;)</title>\n') #.encode('utf-8'))
         self.file.write(u'<meta charset="UTF-8" />\n')
         self.file.write(u'</head>\n')
         self.file.write(u'<body>\n')



    def process_item(self, item, spider):
#      strFile = [] u'<a href="{}">{}</a>' 
#           for aUrl in item:
#              line = json.dumps(aUrl['url']) + "\n"
#              line = json.dumps(aUrl['title'], ensure_ascii=False) + "\n"
        i = 0
        while i < len(item['url']):
            strFile = u'<a href="'+item['url'][i]+u'">'+item['title'][i]+u'</a> Date:'+item['data'][i]+' Cost:'+item['cost'][i]+u'<br>\n'
            i += 1
            self.file.write(strFile) #.encode('utf-8'))

#            self.file.write(item)
#            self.file.write(title)
#            self.file.write(str(ii['data'])) 
#            self.file.write(str(ii['cost']))
#            print('!--> ', ii)
#       line = json.dumps(dict(item), ensure_ascii=False, indent=4) + "\n"
#OrderedDict(item)
#       self.file.write(line)
        return item
    
    def spider_closed(self, spider):
        self.file.write(u'</body>\n')
        self.file.write(u'</html>\n')
        self.file.close() 

