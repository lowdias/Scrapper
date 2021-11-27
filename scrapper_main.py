# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:39:52 2020

@author: ILIAS KAMAL
"""

from db_api import Scrap_bbc_landing, dbmongo_query_articles, dbmongo_clear



if __name__ == '__main__':
    Scrap_bbc_landing()

#Non case sensitive search for a word in the article scrapped
dbmongo_query_articles("covid")

#dbmongo_clear("bbc")



