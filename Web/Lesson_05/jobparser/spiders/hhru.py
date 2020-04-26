# -*- coding: utf-8 -*-
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?clusters=true&enable_snippets=true&text=python&L_save_area=true&area=113&from=cluster_area&showClusters=true']

    def parse(self, response: HtmlResponse):
        next_page = response.css("a.HH-Pager-Controls-Next::attr(href)").extract_first()
        vacansy_links = response.xpath("//a[@class='bloko-link HH-LinkModifier']/@href").extract()
        for link in vacansy_links:
           yield response.follow(link, callback=self.vacancy_parse)
        yield response.follow(next_page, callback=self.parse)

    def vacancy_parse(self, response: HtmlResponse):
        name = response.css('div.vacancy-title h1::text').extract_first()
        salary = response.xpath("//p[@class='vacancy-salary']/span/text()").extract()
        link = response.url
        yield JobparserItem(name=name, salary=salary, link = link)