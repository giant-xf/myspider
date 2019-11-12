# -*- coding: utf-8 -*-
import scrapy
import re
from copy import deepcopy

class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['http://book.suning.com/']

    def parse(self, response):
        # 1.获取大分类的分组
        dl_list = response.xpath("//div[@class='menu-item']/dl")
        for dl in dl_list:
            item = {}
            item["b_cate"] = dl.xpath(".//h3/a/text()").extract_first()
            # 2.获取小分类的分组
            a_list = dl.xpath("./dd/a")
            for a in a_list:
                item["s_href"] = a.xpath("./@href").extract_first()

                item["s_cate"] = a.xpath("./text()").extract_first()
                if item["s_href"] is not None:
                    yield scrapy.Request(
                        url=item["s_href"],
                        callback=self.parse_book_list,
                        meta={"item":deepcopy(item)},
                    )

    def parse_book_list(self,response):
        '''获取图书列表'''
        item = deepcopy(response.meta["item"])
        # 图书列表页分组
        li_list = response.xpath("//div[@id='filter-results']//ul/li")
        for li in li_list:
            item["book_title"] = li.xpath(".//div[@class='res-img']//img/@alt").extract_first()
            item["book_img"] = li.xpath(".//div[@class='res-img']//img/@src").extract_first()
            if item["book_img"] is None:
                item["book_img"] = 'https:'+li.xpath(".//div[@class='res-img']//img/@src2").extract_first()
            item["book_href"] = "https:"+li.xpath(".//div[@class='res-img']//a/@href").extract_first()
            if item["book_href"] is not None:
                yield scrapy.Request(
                    url=item["book_href"],
                    callback=self.parse_book_detail,
                    meta={"item":deepcopy(item)}
                )


        # 获取下一页的url
        # 当下一页的地址是由js生成的，使用正则提取相关的数据拼接下一页的地址
        # page_count = int(re.findall(r"var pagecount=(.*?);",response.body.decode())[0])
        # current_page = int(re.findall(r"var currentpage=(.*?);",response.body.decode())[0])
        # if current_page<page_count:
        #     next_url = item["book_href"]+"?pageNumber={}&sort=0".format(current_page+1)
        #     yield scrapy.Request(
        #         url=next_url,
        #         callback=self.parse_book_list,
        #         meta={"item": response.meta["item"]}
        #     )

        # 当获响应结果有下一页链接时，直接提取到下一页的href
        next_url = response.xpath("//a[@title='下一页']/@href").extract_first()
        if next_url is not None:
            next_url = "https://list.suning.com/"+next_url
            yield scrapy.Request(
                url=next_url,
                callback=self.parse_book_list,
                meta={"item":response.meta["item"]}
            )

    def parse_book_detail(self,response):
        '''图书详情页'''
        item = response.meta["item"]

        item["book_author"] = response.xpath("//ul[@class='bk-publish clearfix']/li[1]/text()").extract_first()
        if item["book_author"] is not None:
            item["book_author"] = item["book_author"].strip()
        item["book_press"] = response.xpath("//ul[@class='bk-publish clearfix']/li[2]/text()").extract_first().strip()
        item["book_publishdata"] = response.xpath("//ul[@class='bk-publish clearfix']/li[3]/span[2]/text()").extract_first()
        item["book_seller"] = re.findall(r"\"shopName\":.*\"(.*?)\"",response.body.decode())[0]
        item["book_price"] = re.findall(r"\"itemPrice\":.*\"(.*?)\"",response.body.decode())
        item["book_price"] = item["book_price"][0]  if len(item["book_price"] )>0 else None
        # print(item)
        yield item




