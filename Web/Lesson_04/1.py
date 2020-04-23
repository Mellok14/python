from lxml import html
from requests import get
from pprint import pprint
from datetime import datetime
from pymongo import MongoClient

header= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}

def mail_news():
    response = get('https://news.mail.ru/', headers = header)
    root = html.fromstring(response.text)
    items = root.xpath("//a[@class='newsitem__title link-holder'] | "
                    "//a[@class='link link_flex'] | "
                    "//a[@class='list__text'] | "
                    "//a[@class='photo photo_small photo_scale photo_full js-topnews__item']  ")
    result = []
    for item in items:
        info = {}
        response = get('https://news.mail.ru/' + (str(item.xpath(".//@href")).replace("['", "")).replace("']", ""), headers=header)
        root = html.fromstring(response.text)
        info['name'] = root.xpath("//h1[@class='hdr__inner']/text()")
        info['link'] = 'https://news.mail.ru/' + (str(item.xpath(".//@href")).replace("['", "")).replace("']", "")
        info['source'] = root.xpath("//span[@class='breadcrumbs__item']//span[@class='link__text']/text()")
        date = str(root.xpath("//span[contains(@class,'note')]/@datetime")).replace("['", "").replace("+03:00']", "").replace("T", " ")
        info['date'] = date
        result.append(info)
    return result

def yandex_news():
    response = get('https://yandex.ru/news/', headers = header)
    root = html.fromstring(response.text)
    items = root.xpath("//div[@class='card__body']")
    result = []
    for item in items:
        info = {}
        info['name'] = item.xpath(".//a[@class='Link link card__link link-like link-like_type_turbo-navigation-react']/text()")
        info['link'] = item.xpath(".//a[@class='Link link card__link link-like link-like_type_turbo-navigation-react']/@href")
        info['source'] = item.xpath(".//@aria-label")
        data = str(datetime.now())[:11]
        info['date'] = data + (str(item.xpath(".//span[@class ='sport-date card__source-date']/text()")).replace("['", "")).replace("']", "")
        result.append(info)
    return result

def lenta_news():
    response = get('https://lenta.ru/', headers = header)
    root = html.fromstring(response.text)
    items = root.xpath("//div[@class='first-item'] | //div[@class='item']")
    result = []
    for item in items:
        info = {}
        info['name'] = str(item.xpath(".//a/text()")).replace("\\xa0", " ")
        info['link'] = 'https://lenta.ru/' + item.xpath("a/@href")[0]
        info['source'] = 'https://lenta.ru/'
        info['date'] = str(datetime.now())[:11] + str(item.xpath(".//a/time/text()")).replace("['", "").replace("']", "")
        result.append(info)
    return result

client = MongoClient('localhost', 27017)
db = client['news']

def to_db(resource):
    for i in resource:
        db.news.insert_one(i)

to_db(mail_news())
to_db(yandex_news())
to_db(lenta_news())

