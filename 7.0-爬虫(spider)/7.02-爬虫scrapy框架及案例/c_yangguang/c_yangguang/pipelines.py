# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import re
from pymongo import MongoClient


class CYangguangPipeline(object):
    def open_spider(self,spider):
        '''在爬虫执行之前执行'''
        client = MongoClient(host=spider.settings.get("MONGO_HOST",""))
        self.collection = client["yangguang"]["xinxi"]

    def process_item(self, item, spider):
        item["content"] = self.process_content(item["content"])
        self.collection.insert(dict(item))
        # print(item)
        return item

    def process_content(self,content):
        content = [re.sub(r"\xa0|\s", "",i) for i in content] # 将xa0替换成空字符串
        content = [i for i in content if len(i)>0] # 将空字符串舍去，只去列表中的有效字符串
        return content