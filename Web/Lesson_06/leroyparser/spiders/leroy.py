# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from leroyparser.items import LeroyparserItem
from scrapy.loader import ItemLoader

class LeroySpider(scrapy.Spider):
    name = 'leroy'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        self.start_urls = [f'https://leroymerlin.ru/search/?sortby=8&tab=products&q={search}']

    def parse(self, response: HtmlResponse):
        next_page = 'https://leroymerlin.ru/' + str(response.xpath("//div[@class='next-paginator-button-wrapper']/a/@href").extract_first())
        ads_links = response.xpath("//div[@class='product-name']/a/@href").extract()
        for link in ads_links:
            yield response.follow(link, callback=self.parse_ads)
        yield response.follow(next_page, callback=self.parse)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=LeroyparserItem(), response=response)
        loader.add_xpath('name',"//h1[@class='header-2']/text()")
        loader.add_xpath('price', "//span[@slot='price']/text()")
        loader.add_xpath('parameters', "//div[@class='def-list__group']//text()")
        loader.add_xpath('photos',"//picture/source[@media=' only screen and (min-width: 1024px)']/@srcset")
        yield loader.load_item()
