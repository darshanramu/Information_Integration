#!/usr/bin/env python
import re
from tutorial.items import ProductItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
count = 0
class ProductSpider(CrawlSpider):
    name = "spiderman"
    allowed_domains = ["www.ebay.com"]
    start_urls = ["http://www.ebay.com/sch/"]
    rules = (Rule(LinkExtractor(allow=(['/itm/','_pgn','-Shoes-'])), callback="parse_items", follow= True),)

    def parse_items(self, response):
        global count
        x = response.xpath("//div[@id='CenterPanelInternal']")
    	#print x
    	if x:
       		for sel in x:
       			    #print sel	
			    item = ProductItem()
			    item['price'] = sel.xpath("//span[@id='prcIsum']/text()").extract()
			    item['title'] = sel.xpath("//h1[@id='itemTitle']/text()").extract()
			    item['link'] = response.url
			    print item
			    if re.search('shoe',str(item['title'][0]), re.IGNORECASE):
				    price = -1
				    try:
				    	price = item['price'][0][4:]
				    except:
				    	pass
				    if float(price)>0.0 and float(price)<300.00:
				    	    count+=1
					    print count
					    with open("webpages/result"+str(count)+".html","wb") as f:
						 f.write(response.body)
					    with open("item_links","a") as i:
						 i.write(str(item)+'\n')
				    if count==1000:
				    	raise CloseSpider('Downloaded 1000 pages')
