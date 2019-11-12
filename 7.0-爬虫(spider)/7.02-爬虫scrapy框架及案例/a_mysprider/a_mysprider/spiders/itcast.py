# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast' # 爬虫的名字<启动爬虫时使用：scrapy crawl itcast>
    allowed_domains = ['itcast.cn']     # 限定爬取的网址，防止爬取到别的网址
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # response.xpath("//div[@class='tea_con']//h3/text()")返回值是对象
        # <Selector xpath="//div[@class='tea_con']//h3/text()" data='周老师'>,
        # ret = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret)

        list = response.xpath("//div[@class='tea_con']//li")
        # content_list = []
        for li in list:
            item = {}
            # item['name'] = li.xpath(".//h3/text()").extract()[0]
            # item['title'] = li.xpath(".//h4/text()").extract()[0]
            item['name'] = li.xpath(".//h3/text()").extract_first()
            item['title'] = li.xpath(".//h4/text()").extract_first()
            # Spider must return Request, BaseItem, dict or None,
            # print(item)
            logger.warning(item)
            yield item
        #     content_list.append(item)
        # yield content_list



