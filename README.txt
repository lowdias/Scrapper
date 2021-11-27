Install the packages in requirements.txt and install mongodb and ideally Robo 3T for better visualisation,
in scrapper_main.py execute every function one by one, do not execute the whole script in one go!!!!

Scrap_bbc_landing():
Scraps the landing page of http://bbc.com and store the scrapped articles in the bbc database of the 
local mongodb server(localhost) port:27017

dbmongo_query_articles("China"):
Non case sensitive search for the word China in the articles scrapped.

The mongo database is hosted on the cloud at cloud.mongodb.com

