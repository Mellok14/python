from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from leroyparser import settings
from leroyparser.spiders.leroy import LeroySpider



if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroySpider, search='кран')

    process.start()