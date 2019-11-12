# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import urllib
import json

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com','p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        # 图书大分类分组
        dt_list = response.xpath("//div[@class='mc']/dl/dt")
        for dt in dt_list:
            item = {}
            item["b_cate"] = dt.xpath("./a/text()").extract_first()
            # 图书大分类中小分类分组
            em_list = dt.xpath("./following-sibling::dd[1]/em")
            for em in em_list:
                item["s_cate"] = em.xpath("./a/text()").extract_first()
                item["s_href"] = em.xpath("./a/@href").extract_first()
                if item["s_href"] is not None:
                    item["s_href"] = 'https:'+item["s_href"]
                yield scrapy.Request(
                    url=item["s_href"],
                    callback=self.parse_book_list,
                    meta={'item':deepcopy(item)}
                )

    def parse_book_list(self,response):
        '''解析大分类中图书列表'''
        item = response.meta['item']
        # 分组
        li_list = response.xpath("//ul[@class='gl-warp clearfix']/li[@class='gl-item']")
        for li in li_list:
            item["book_name"] = li.xpath(".//div[@class='p-name']//em/text()").extract_first().strip()
            item["book_img"] = li.xpath(".//div[@class='p-img']//img/@src").extract_first()
            # if item["book_img"] is None:
            #     item["book_img"] = li.xpath(".//div[@class='p-img']//img/@src").extract_first()
            item['book_img'] = urllib.parse.urljoin(response.url,item["book_img"])
            item["book_author"] = li.xpath(".//span[@class='author_type_1']/a/text()").extract()
            item["book_press"] = li.xpath(".//span[@class='p-bi-store']/a/text()").extract_first()
            item["book_publish_data"] = li.xpath(".//span[@class='p-bi-date']/text()").extract_first().strip()
            # item["book_seller"] = li.xpath(".//div[@class='p-shopnum']/span/text()").extract_first()
            item["book_href"] = li.xpath(".//div[@class='p-name']/a/@href").extract_first()
            item["book_sku"] = li.xpath(".//div[@class='gl-i-wrap j-sku-item']/@data-sku").extract_first()

            if item["book_sku"] is not None:
                sku_url = "https://p.3.cn/prices/mgets?&skuIds={}".format(item["book_sku"])
                yield scrapy.Request(
                    url=sku_url,
                    callback=self.parse_price,
                    meta={'item':deepcopy(item)}
                )

            # 访问详情页获取数据
            # if item["book_href"] is not None:
            #     item["book_href"] = urllib.parse.urljoin(response.url,item["book_href"])
            #     yield scrapy.Request(
            #         url=item["book_href"],
            #         callback=self.parse_book_detail,
            #         meta={'item':deepcopy(item)}
            #     )

        # 列表翻页
        next_url = response.xpath("//a[@class='pn-next']/@href").extract_first()
        if next_url is not None:
            next_url = urllib.parse.urljoin(response.url,next_url)
            yield scrapy.Request(
                url=next_url,
                callback=self.parse_book_list,
                meta={'item':item}
            )


    def parse_price(self,response):
        '''获取价格'''
        item = response.meta["item"]
        item['book_price'] = json.loads(response.body.decode())[0]['op']
        print(item)

    def parse_book_detail(self,response):
        '''获取详情页数据'''
        item = response.meta['item']

        # item["book_detail_content"] = response.xpath("//div[@class='book-detail-content']/p/text()").extract_first()
        # item["book_author_content"] = response.xpath("//div[@class='book-detail-content']/text()").extract()
        #



