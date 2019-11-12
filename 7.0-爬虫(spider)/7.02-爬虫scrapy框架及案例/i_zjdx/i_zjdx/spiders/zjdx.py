# -*- coding: utf-8 -*-
import scrapy


class ZjdxSpider(scrapy.Spider):
    name = 'zjdx'
    allowed_domains = ['person.zju.edu.cn']
    start_urls = ['https://person.zju.edu.cn/server/api/front/codes/key/subject/codes?codetype=3&lang=cn']

    def parse(self, response):
        print(response)
