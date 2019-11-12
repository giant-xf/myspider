# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

client = MongoClient(host="192.168.43.150",port=27017)
collection = client["tencent"]["hr"]

class BTencentPipeline(object):
    def process_item(self, item, spider):
        print(item)
        # 向数据库中插入数据,只能插入字典
        collection.insert(dict(item))
        return item
