from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import os
import sys

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from jobparser import settings
from jobparser.spiders.hhru import HhruSpider
from jobparser.spiders.sjru import SjruSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(HhruSpider)
    process.crawl(SjruSpider)
    process.start()