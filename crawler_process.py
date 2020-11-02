# from scrapy import cmdline
#
# cmdline.execute()
import sys
from scrapy import spiderloader
from scrapy.utils import project
from scrapy.crawler import CrawlerProcess


def crawler_process(process_num, spider_class):
    process = CrawlerProcess()
    for _ in range(int(process_num)):
        process.crawl(spider_class)
    process.start()


if __name__ == '__main__':
    settings = project.get_project_settings()
    spider_loader = spiderloader.SpiderLoader.from_settings(settings)
    spiders = spider_loader.list()
    classes = [spider_loader.load(name) for name in spiders]
    spider_class_map = {x: y for x, y in zip(spiders, classes)}
    xxx = [sys.argv[1], spider_class_map[sys.argv[2]]]
    crawler_process(*xxx)
