# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DBaidutiebaPipeline(object):
    def process_item(self, item, spider):
        spider.settings.get("MONGO_HOST",'')    # 获取配置文件中的配置属性
        print(item["title"])
        return item
