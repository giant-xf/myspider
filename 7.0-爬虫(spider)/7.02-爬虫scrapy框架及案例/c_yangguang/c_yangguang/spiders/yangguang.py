# -*- coding: utf-8 -*-
import scrapy
from  c_yangguang.items  import CYangguangItem

class YangguangSpider(scrapy.Spider):
    name = 'yangguang'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/html/top/reply.shtml']

    def parse(self, response):
        # 给tr分组
        tr_list = response.xpath("//div[@class='newsHead clearfix']/table[2]//tr")
        for tr in tr_list:
            item = CYangguangItem()
            item["title"] = tr.xpath("./td[3]/a/@title").extract_first()
            item["href"] = tr.xpath("./td[3]/a/@href").extract_first()
            item["name"] = tr.xpath("./td[5]/text()").extract_first()
            item["publish_data"] = tr.xpath("./td[last()]/text()").extract_first()

            # 构造详情页的请求
            yield scrapy.Request(
                url=item['href'],
                callback=self.parse_detail,
                # 利用meta将item传给回调(callback)函数
                meta={"item":item},
            )

        # 请求下一页的地址
        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                url=next_url,
                callback=self.parse,
            )

    def parse_detail(self,response):
        item = response.meta['item']
        item["content"] = response.xpath("//div[@class='wzy1']//table[2]//tr[1]/td/text()").extract()
        item["content_img"] = response.xpath("//div[@class='wzy1']//table[2]//tr[1]/td//img/@src").extract()
        item["content_img"] = ['http://wz.sun0769.com'+i for i in item["content_img"]]

        yield item


