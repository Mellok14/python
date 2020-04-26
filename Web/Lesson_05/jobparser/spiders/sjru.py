# -*- coding: utf-8 -*-
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class SjruSpider(scrapy.Spider):
    name = 'sjru'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://russia.superjob.ru/vacancy/search/?keywords=python']

    def parse(self, response: HtmlResponse):
        next_page = 'https://russia.superjob.ru' + str(response.xpath("//a[@class='icMQ_ _1_Cht _3ze9n f-test-button-dalshe f-test-link-Dalshe']/@href").extract_first())
        vacansy_links = response.xpath("//div[@class='_3mfro CuJz5 PlM3e _2JVkc _3LJqf']/a/@href").extract()
        for link in vacansy_links:
           yield response.follow(link, callback=self.vacancy_parse)
        yield response.follow(next_page, callback=self.parse)

    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath("//h1[@class='_3mfro rFbjy s1nFK _2JVkc']/text()").extract_first()
        salary = response.xpath("//span[@class='_3mfro _2Wp8I ZON4b PlM3e _2JVkc']/text()").extract()
        link = response.url
        yield JobparserItem(name=name, salary=salary, link = link)