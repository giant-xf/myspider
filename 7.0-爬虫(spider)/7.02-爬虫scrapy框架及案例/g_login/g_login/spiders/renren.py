# -*- coding: utf-8 -*-
import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/972184968/newsfeed/photo']

    def start_requests(self):
        cookies = 'anonymid=k08c658fi8jk5h; _r01_=1; ln_uact=13269764268; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=cd78dc21-4d64-417c-b013-3701c998f99a%7C6ed4fe0e013c40f75b477aa3eb9e5677%7C1567841272092%7C1%7C1567841275002; _ga=GA1.2.1527801894.1567841807; depovince=GW; _de=B9FE8FE7AAC97B95DE2F500122E863BC; jebecookies=e6c1fce9-dd95-4a60-8829-4e27754db305|||||; ick_login=2ecc73ab-c447-4d7d-9968-f6955f3847a5; p=e3284feee9b1709c268d85799285f45d8; first_login_flag=1; t=f96e30665b89857088946f399a9ed24b8; societyguester=f96e30665b89857088946f399a9ed24b8; id=972184968; xnsid=a1b4ce82; ver=7.0; loginfrom=null'
        # 将cookies转换成字典
        cookies = {i.split('=')[0]: i.split("=")[1] for i in cookies.split('; ')}
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall(r'李成家',response.body.decode()))
        yield scrapy.Request(
            url='http://www.renren.com/972184968/profile',
            callback=self.parse_detail,
        )

    def parse_detail(self,response):
        print(re.findall(r'大学',response.body.decode()))
