# -*- coding: utf-8 -*-
import scrapy
import re

class Github2Spider(scrapy.Spider):
    name = 'github2'
    # allowed_domains = ['github.com']
    # start_urls = ['http://github.com/login']
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            # formdata={'login':"giant-xf",'password':'819989150@163.com'},
            formdata={'email': '13269764268', 'password': '88888888a'},
            callback=self.after_login
        )

    def after_login(self,response):
        '''登入后处理'''
        print(re.findall(r"李成家",response.body.decode()))

