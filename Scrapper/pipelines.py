# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#
# cd C:\Program Files\MongoDB\Server\4.2\bin
#mongod
import pymongo

from Scrapper.settings import MONGODB_SERVER, MONGODB_PORT, MONGODB_COLLECTION, MONGODB_DB
from scrapy.exceptions import DropItem
import logging
#from scrapy import log





class MongoDBPipeline(object):

    def __init__(self):
        
        connection = pymongo.MongoClient(
           MONGODB_SERVER,
            MONGODB_PORT
        )
        db = connection[MONGODB_DB]
        self.collection = db[MONGODB_COLLECTION]
        
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            logging.log(level=logging.DEBUG, msg="Article added to MongoDB database!")
        return item