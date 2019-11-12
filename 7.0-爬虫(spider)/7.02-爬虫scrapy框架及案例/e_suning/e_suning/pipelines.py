# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class ESuningPipeline(object):
    def open_spider(self,spider):
        '''在爬虫执行之前执行'''
        client = MongoClient(host=spider.settings.get("MONGO_HOST", ""))
        self.collection = client["suning"]["xinxi"]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        print(item['book_title'])
        return item
