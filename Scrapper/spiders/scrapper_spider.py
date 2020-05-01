# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 04:06:42 2020

@author: PC GAMER
"""
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from Scrapper.items import StackItem

class ScrapperSpider(Spider):
    name = "Scrap_bbc"
    
    # allowed_domains = ["stackoverflow.com"]
    # start_urls = ["http://stackoverflow.com/questions?pagesize=50&sort=newest"]
    allowed_domains = ["bbc.com"]
    
    start_urls = ["http://bbc.com"]
   
    # def parse(self, response):
    #     questions = Selector(response).xpath('//div[@class="summary"]/h3')
        
        
    #     for question in questions:
    #         item = StackItem()
    #         item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
    #         item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
    #         yield item
            
    def parse(self, response):
            
       
        item = StackItem()
        item['title'] = response.css('head > title::text').get()
        item['url'] = response.url
        item['body'] = response.css('div.story-body__inner > p::text').extract()
        item['body'] = "".join(item['body'])
        if item['body'] == [] :
            item['body'] = response.css('div.body-content > p::text').extract()
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