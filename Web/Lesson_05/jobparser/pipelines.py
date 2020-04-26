# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class JobparserPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vacansy_hh_sj

    def process_item(self, item, spider):
        item = dict(item)
        if spider.name == 'hhru':
            self.salary_hh(item)
        else:
            self.salary_sj(item)
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item

    def salary_hh(self, item):
        if item['salary'][0] == 'до ':
            item['max_salary']= item['salary'][1].replace('\xa0', '')
            item['min_salary']= None
            item['currency'] = item['salary'][3]
        elif len(item['salary']) == 7:
            item['min_salary']= item['salary'][1].replace('\xa0', '')
            item['max_salary']= item['salary'][3].replace('\xa0', '')
            item['currency'] = item['salary'][5]
        elif len(item['salary']) == 1:
            item['max_salary']= None
            item['min_salary']= None
            item['currency'] = None
        else:
            item['min_salary']= item['salary'][1].replace('\xa0', '')
            item['max_salary']= None
            item['currency'] = item['salary'][3]
        item.pop('salary', None)

    def salary_sj(self, item):
        if item['salary'][0] == 'до':
            item['max_salary']= item['salary'][2].split('\xa0')[0] + item['salary'][2].split('\xa0')[1]
            item['min_salary']= None
            item['currency'] = item['salary'][2].split('\xa0')[2]
        elif len(item['salary']) == 3 and item['salary'][0] == 'от':
            item['min_salary']= item['salary'][2].split('\xa0')[0] + item['salary'][2].split('\xa0')[1]
            item['max_salary']= None
            item['currency'] = item['salary'][2].split('\xa0')[2]
        elif len(item['salary']) == 1:
            item['max_salary']= None
            item['min_salary']= None
            item['currency'] = None
        else:
            item['min_salary']= item['salary'][0].replace('\xa0')
            item['max_salary']= item['salary'][1].replace('\xa0')
            item['currency'] = item['salary'][3]
        item.pop('salary', None)