# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 04:06:42 2020

@author: ILIAS KAMAL
"""
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from Scrapper.items import StackItem

class ScrapperSpider(Spider):
    name = "Scrap_bbc"
    
    # allowed_domains = ["stackoverflow.com"]
    # start_urls = ["http://stackoverflow.com/questions?pagesize=50&sort=newest"]
    #allowed_domains = []
    
    #start_urls = []
   
            
    def parse(self, response):
            
       
        item = StackItem()
        item['title'] = response.css('title::text').get()
        item['url'] = response.url
        item['body'] = response.css('p::text').extract()
        item['body'] = "".join(item['body'])
        if item['body'] == [] :
            item['body'] = response.css('p::text').extract()
            item['body'] = "".join(item['body'])
        yield item
            
        for articles in response.css('a.media__link::attr(href)').extract() :
            if not "http" in articles:
                articles = response.urljoin(articles)
            yield scrapy.Request(articles, callback=self.parse)
        
        

"""

We are iterating through the `questions` and assigning the `title` and `url` values from the scraped data. Be sure to test out the XPath selectors in the JavaScript Console within Chrome Developer Tools - e.g., `$x('//div[@class="summary"]/h3/a[@class="question-hyperlink"]/text()')` and `$x('//div[@class="summary"]/h3/a[@class="question-hyperlink"]/@href')`.

## Test

Ready for the first test? Simply run the following command within the "stack" directory:

```console
$ python - m scrapy crawl stack
"""