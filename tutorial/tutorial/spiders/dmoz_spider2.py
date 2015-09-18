import scrapy
import sys
from tutorial.items import DmozItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

count = 0
class DmozSpider(CrawlSpider):
    name = "dmoz2"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["http://www.amazon.com/s/ref=sr_st_relevancerank?keywords=iphone+6&rh=n%3A2335752011%2Ck%3Aiphone+6&qid=1441485596&sort=relevancerank"]

    rules = (
        Rule(LinkExtractor(allow=("ref=sr_pg_*")), callback="parse_items_1", follow= True),
        )

    def parse_items_1(self, response):
        global count
    	
    	#print response.url
    	x = response.xpath("/html/body/div/div/div/div/div/h1/span")
    	#x = response.xpath("/html/body/div/div/div/div/div[@id='price']/tabl")
    	if x:
    		#print x
    		for sel in x:
			    item = DmozItem()
			    item['price'] = sel.xpath("//table//span[@id='priceblock_ourprice']/text()").extract()
			    item['title'] = sel.xpath('/html/body/div/div/div/div/div/h1/span/text()').extract()
			    item['link'] = response.url
			    count+=1
			    with open("result"+str(count)+".html","wb") as f:
			    	f.write(response.body)
			    
			    #yield item"""
			    print item
			    
		if count==3:
			return
    		
    	else:
    		print "Empty"
