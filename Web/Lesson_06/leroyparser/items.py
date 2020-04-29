# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Identity,Compose

def cleaner_price(value):
    value = int(value[0])
    return value

#Преобразовывает любые характеристики товара к словарю: "Материал: латунь" и т.д.
def cleaner_parameters(value):
    for n, i in enumerate(value):
        value[n] = ''.join(i).split()
    value_1 = [x for x in value if x]
    value_1 = [' '.join(x) for x in value_1]
    value = dict(zip(*[iter(value_1)] * 2))
    return value

class LeroyparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(cleaner_price))
    parameters = scrapy.Field(input_processor=Compose(cleaner_parameters))
    photos = scrapy.Field(output_processor=Identity())