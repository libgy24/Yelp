# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import item,Field


class YelpItem(scrapy.Item):
    # define the fields for your item here like:
    restaurant = Field()
    city = Field()
    address = Field()

    review = Field()
    review_date =Field()
    vote = Field()
    useful_vote = Field()
    funny_vote = Field()
    cool_vote = Field()
    review_image = Field()


