import scrapy
import sys,re
from tutorial.items import PhoneItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
count = 0
class PhoneSpider(CrawlSpider):
    name = "spiderman"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=TV"]
    rules = (Rule(LinkExtractor(allow=(['/dp/','/ref=sr_pg_/'])), callback="parse_link", follow= True),)

    def parse_link(self, response):
        global count
        #print response.url
        
    	x = response.xpath("/html/body/div/div/div/div/div/h1/span")
    	if x:
       		for sel in x:
			    item = PhoneItem()
			    item['price'] = sel.xpath("//table//span[@id='priceblock_ourprice']/text()").extract()
			    #item['sale_price'] = sel.xpath("//table//span[@id='priceblock_ourprice']/text()").extract()
			    item['title'] = sel.xpath('/html/body/div/div/div/div/div/h1/span/text()').extract()
			    item['link'] = response.url
			    if(re.search('LG', str(item['title'][0]), re.IGNORECASE)) and (re.search('TV', str(item['title'][0]), re.IGNORECASE)):
				    #print item
				    #print "details=",item['price'][0][1:]
				    price = -1
				    try:
				    	price = item['price'][0][1:]
				    except:
				    	pass
				    if float(price)>0.0 and float(price)<100000.00:
				    	    #print "INSIDE************"
					    count+=1
					    with open("webpages/result"+str(count)+".html","wb") as f:
						 f.write(response.body)
					    with open("item_links","a") as i:
						 i.write(str(item)+'\n')
				    #else:
				    #	print "PRICE=",price
   	else:
    		print "Empty"
    		
    		
