# coding=utf-8

import requests
import json
from lxml import etree
import re
from urllib import parse

class TiebaSpider(object):
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
        self.start_url = 'https://tieba.baidu.com/f?ie=utf-8&kw='+tieba_name+'&fr=search&pn=0'
        self.part_url = 'http://tieba.baidu.com'

    def parse_url(self, url):
        '''发送请求，获取响应'''
        print("当前请求的地址:",url)
        html_str = requests.get(url, headers=self.headers)
        # 带有编码的不能用decode，只能使用byte
        html_str = html_str.content.decode()

        sub_str =r'<!--|-->|<--|src="http://aod-image.baidu.com/5/pic/9dc7a97299d6060bc027efbe8ba3c67d.jpg"|src="http://aod-image.baidu.com/5/pic/0c11fb54e3361f72ca4d473f3c5be670.jpg"'

        # 也可以用str.replace('\n','')替换某些字符
        html_str = re.sub(sub_str,'',html_str)
        # html_str = html_str.encode()
        return html_str

    def get_content_list(self,html_str):
        '''提取数据'''
        html = etree.HTML(html_str)
        # html = re.sub(r"<!--|-->",'',html)

        # 或者可以写成"//ul[@id='frslistcontent']/li[contains(@class,'tl_shadow')]"
        # todo：手机版
        # li_list = html.xpath("//ul[@id='frslistcontent']/li[@class='tl_shadow tl_shadow_new']")
        # content_list = []
        # for li in li_list:
        #     item = {}
        #     item['title'] = li.xpath(".//span[@class='']/text()")[0] if len(li.xpath(".//span[@class='']/text()"))>0 else None
        #     item['href'] = li.xpath(".//a/@href")[0] if len(li.xpath(".//a/@href"))>0 else None
        #     item['img_list'] = self.get_img_list(item['href'])
        #     content_list.append(item)
        # todo：电脑版
        # 提取下一页url地址
        next_url = html.xpath("//a[text()='下一页>']/@href")[0] if len(
            html.xpath("//a[text()='下一页>']/@href")) > 0 else None

        li_list = html.xpath("//ul[@id='thread_list']//li[contains(@class,'j_thread_list')]//div[contains(@class,'threadlist_title')]/a") # 分组
        content_list = []
        for li in li_list:
            item = {}
            item['title'] = li.xpath("./text()")[0] if len(li.xpath("./text()"))>0 else None
            item['href'] = self.part_url+li.xpath("./@href")[0] if len(li.xpath("./@href"))>0 else None
            item['img_list'] = self.get_img_list(item['href'], [])
            content_list.append(item)
            # 保存
            self.save_content_list(content_list)
        return content_list, next_url


    def get_img_list(self, detail_url, total_img_list):
        '''获取帖中的所有图片'''
        # 3.2 请求列表页的地址，获取详情页第一页
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)
        # print(etree.tostring(detail_html))
        # 3.3 提取详情页第一页的图片，提取下一页的地址
        img_list = detail_html.xpath("//img[@class='BDE_Image']/@src")
        # total_img_list+=img_list
        total_img_list.extend(img_list)
        # 3.4 请求详情页的下一页地址，进入3.2-3.4循环
        detail_next_url =detail_html.xpath("//a[text()='下一页']/@href")
        # print("当前地址:",detail_next_url)
        if len(detail_next_url)>0:
            detail_next_url = self.part_url + detail_next_url[0]
            # 递归调用
            return self.get_img_list(detail_next_url, total_img_list)
        print('-'*100)
        # print(total_img_list)
        return total_img_list

    def save_content_list(self, content_list):
        '''保存数据'''
        # file_name = '贴吧爬取每个帖子图片/'+self.tieba_name+'.txt'
        file_name = '贴吧爬取每个帖子图片/' + self.tieba_name + '.txt'
        with open(file_name,'a', encoding='utf-8') as f:
            f.write(json.dumps(content_list[0],ensure_ascii=False,indent=2))
            f.write('\n')

        print('保存成功')

    def run(self):
        # 1.start_url
        next_url = self.start_url
        while next_url is not None:
            # 2.发送请求，获取响应
            html_str = self.parse_url(next_url)
            # 3.提取数据，提取下一页url地址
                # 3.1 提取列表页的标题和url地址
                # 3.2 请求列表页的地址，获取详情页第一页
                # 3.3 提取详情页第一页的图片，提取下一页的地址
                # 3.4 请求详情页的下一页地址，进入3.2-3.4循环
            content_list, next_url = self.get_content_list(html_str)
            # 4.保存数据
            self.save_content_list(content_list)
            # 5.请求下一页的url地址，进入2-5步循环


if __name__ == '__main__':
    name = input("请输入要爬取的贴吧名：")
    tieba = TiebaSpider(name)
    tieba.run()







