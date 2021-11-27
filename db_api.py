# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 03:35:48 2020

@author: ILIAS KAMAL
"""

import pymongo
from Scrapper.settings import MONGODB_PORT, MONGODB_COLLECTION, MONGODB_DB, MONGODB_SERVER
from pathos.multiprocessing import ProcessPool
from pathos.threading import ThreadPool
from Scrapper.spiders.scrapper_spider import ScrapperSpider
import time
import sys


def Scrap_bbc_landing():
    pool = ProcessPool(nodes=4)

    def f_runner(spider):
        from twisted.internet import reactor
        from scrapy.settings import Settings
        import Scrapper.settings as my_settings
        from scrapy.crawler import CrawlerProcess, CrawlerRunner
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        runner = CrawlerRunner(settings=crawler_settings)
        deferred = runner.crawl(spider)
        deferred.addBoth(lambda _: reactor.stop())
        reactor.run()


    results = pool.amap(f_runner, [ScrapperSpider])
    t = 0
    while not results.ready():
        time.sleep(5); print(".", end=' '); t= t+5
        if t == 240:
            print("\nProcess stalling...DO NOT EXECUTE THE WHOLE SCRIPT BUT EACH FUNCTION ALONE...EXITING\n"); return None

    pool.clear()

def dbmongo_query_articles(query):
    connection = pymongo.MongoClient(MONGODB_SERVER,MONGODB_PORT)
    db = connection[MONGODB_DB]
    collection = db[MONGODB_COLLECTION]
    array = list(collection.find({'body': {"$regex": query, '$options' : 'i'}}))
    print(*array, sep='\n')
    print("\nNumber of articles found:{}" .format(len(array)))

def dbmongo_clear(query):
    connection = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
    db = connection[MONGODB_DB]
    db.getCollection(query).deleteMany({})






