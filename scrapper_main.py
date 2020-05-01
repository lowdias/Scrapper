# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:39:52 2020

@author: PC GAMER
"""

from db_api import Scrap_bbc_landing , dbmongo_query_articles

#########WARNING############
#Execute every function one by one, do not execute the whole script in one go
############################
#Scrap the landing page of http://bbc.com and store the scrapped articles in 
#the bbc database of the local mongodb server(localhost) port:27017
Scrap_bbc_landing()

#Non case sensitive search for a word in the article scrapped
dbmongo_query_articles("China")



