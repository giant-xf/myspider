# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import re

from  d_baidutieba.items import DBaidutiebaItem
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw="迪丽热巴"']

    def parse(self, response):
        html_str = response.body.decode()
        sub_str = r'<!--|-->|<--|src="http://aod-image.baidu.com/5/pic/9dc7a97299d6060bc027efbe8ba3c67d.jpg"|src="http://aod-image.baidu.com/5/pic/0c11fb54e3361f72ca4d473f3c5be670.jpg"'
        html_str = re.sub(sub_str, '', html_str)
        # 提取数据
        html = etree.HTML(html_str)
        # 分组
        a_list = html.xpath("//ul[@id='thread_list']//li[contains(@class,'j_thread_list')]//div[contains(@class,'threadlist_title')]/a")
        for a in a_list:
            item = DBaidutiebaItem()
            item["title"] = a.xpath("./@title")[0]
            item["title"] = item["title"] if len(item["title"])>0 else None
            item["href"] = "http://tieba.baidu.com"+a.xpath("./@href")[0]
            item["href"] = item["href"] if len(item["href"])>0 else None

            # 访问详情页
            yield scrapy.Request(
                url=item["href"],
                callback=self.parse_detail,
                meta={"item":item},
            )

        # 获取下一页链接
        next_url = response.xpath("//a[text()='下一页>']/@href")
        print('-'*100)
        print(next_url)
        print('-' * 100)
        if len(next_url)>0:
            yield scrapy.Request(
                url="http://tieba.baidu.com"+next_url[0],
                callback=self.parse,
            )

    def parse_detail(self,response):
        # 获取传过来的item
        item = response.meta["item"]
        html_str = response.body.decode()
        sub_str = r'<!--|-->|<--|src="http://aod-image.baidu.com/5/pic/9dc7a97299d6060bc027efbe8ba3c67d.jpg"|src="http://aod-image.baidu.com/5/pic/0c11fb54e3361f72ca4d473f3c5be670.jpg"'
        html_str = re.sub(sub_str, '', html_str)
        # 提取数据
        html = etree.HTML(html_str)
        item["img_list"] = html.xpath("//img[@class='BDE_Image']/@src")
        item["img_list"] = item["img_list"] if len(item["img_list"])>0 else None
        # 访问下一页
        next_url = response.xpath("//a[text()='下一页']/@href")
        # if len(next_url)>0:
        #     yield scrapy.Request(
        #         url="http://tieba.baidu.com"+next_url[0],
        #         callback=self.parse_detail
        #     )
        yield item
