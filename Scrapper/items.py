# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 00:53:46 2020

@author: ILIAS KAMAL
"""

import scrapy
from scrapy.item import Item, Field


class StackItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    url = Field()
    body = Field()
    pass