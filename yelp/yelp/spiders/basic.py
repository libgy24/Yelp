# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["web"]
    start_urls = ['http://web/:yelp.com/minneapolis']

    def parse(self, response):
        pass
