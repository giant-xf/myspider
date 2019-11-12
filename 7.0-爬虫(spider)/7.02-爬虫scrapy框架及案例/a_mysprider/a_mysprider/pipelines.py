# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import logging
# logger = logging.getLogger(__name__)
from .spiders.itcast import logger

class AMyspriderPipeline(object):
    def process_item(self, item, spider):
        # print(item)
        # item['hello'] = "python"
        logger.warning("-"*20)
        return item

# class AMyspriderPipeline1(object):
#     def process_item(self, item, spider):
#         print(item)
#         return item