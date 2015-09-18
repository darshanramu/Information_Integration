#!/usr/bin/env python
import re
from craigslist.items import craigslistItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy.utils.markup import remove_tags
"""
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
"""    
count = 0

class craigSpider(CrawlSpider):
    name = "craig"
    allowed_domains = ["losangeles.craigslist.org"]
    start_urls = ["https://losangeles.craigslist.org/search/sya?query=laptop"]
    rules = (Rule(LinkExtractor(allow=(['/sys/','/sya'])), callback="parse_items", follow= True),)

    def parse_items(self, response):
        global count
        x = response.xpath("//section[@class='userbody']")
    	#print x
    	
	if x:
       		for sel in x:
       			    #print sel	
			    item = craigslistItem()
			    #item['title'] = sel.xpath("//span[@class='postingtitletext']/text()").extract()
			    #item['link'] = response.url
			    item['desc'] = remove_tags(sel.xpath("//section[@id='postingbody']").extract()[0].replace('<br>',' ').replace('\n',' '))
			    #for i in item['desc']
			    print item['desc']
			    count+=1
			    print "Pages so far = ", count
			    with open("item_desc","a") as i:
					i.write(str(item['desc'])+'\n')
					
			    '''if re.search('shoe',str(item['title'][0]), re.IGNORECASE):
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
						 i.write(str(item)+'\n')'''
			    if count==2000:
			    	    	raise CloseSpider('Downloaded 2000 pages')
