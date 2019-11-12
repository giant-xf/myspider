# -*- coding: utf-8 -*-
import scrapy
from b_tencent.items import BTencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    '''
    https://careers.tencent.com/search.html?query=ot_40001001,ot_40001002,ot_40001003,ot_40001004,ot_40001005,ot_40001006
    https://careers.tencent.com/search.html?query=ot_40001001,ot_40001002,ot_40001003,ot_40001004,ot_40001005,ot_40001006&index=2
    '''

    def parse(self, response):
        # 分组
        tr_list = response.xpath('//table[@class="tablelist"]/tr')[1,-1]
        for tr in tr_list:
            item = BTencentItem()
            item["title"] = tr.xpath("./td[1]/a/text()").extract_first()
            item["position"] = tr.xpath("./td[2]/text()").extract_first()
            item["publish_data"] = tr.xpath("./td[5]/text()").extract_first()
            yield item

        # 找到下一页的链接
        next_url = response.xpath("//a[@id='next']/@href").extract_first()
        if next_url != "javascript;":
            next_url = 'https://hr.tencent.com/'+next_url
            # 构造request对象
            yield scrapy.Request(
                url=next_url,
                # 由于处理对象的方式是一模一样的直接调用自己的，否则重写parse方法
                callback=self.parse,
                # meta={"item":item}
            )


    # def parse1(self,response):
    #     item = response.meta["item"]


