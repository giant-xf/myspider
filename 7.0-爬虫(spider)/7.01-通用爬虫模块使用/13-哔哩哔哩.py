# coding=utf-8

import re
import requests
import json
from lxml import etree

class BiLi(object):
    '''哔哩哔哩爬取弹幕'''
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

        self.bili_url = 'https://www.bilibili.com/v/douga'
        # 哔哩哔哩弹幕url
        self.danmu_url = 'https://comment.bilibili.com/{}.xml'

        self.url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=15&rid={}'

        self.bili_video_url = 'https://www.bilibili.com/video/av{}'
    # def get_video_url(self,url):
    #     '''获取视频的链接地址'''
    #     # 发送请求，获取首页数据
    #     bili_html = self.parse_url(self.bili_url)
    #     # 将获取到的html转换成etree对象
    #     html = etree.HTML(bili_html)
    #     print(etree.tostring(html))
    #     # etree对象分组
    #     li_list = html.xpath("//div[@class='channel-m']")
    #     # // div[ @class ='channel-m']//div[@ class ='spread-module']//a/@ href
    #     # // div[ @class ='channel-m']//li[contains( @class ,'rank-item')]//a/@ href
    #     content_list = []
    #     for list in li_list:
    #         li = []
    #         li_left = list.xpath("//div[@ class ='spread-module']//a/@href") # ['1','2']
    #         li_right = list.xpath("//li[contains( @class ,'rank-item')]//a/@ href")
    #         li = li_left + li_right
    #         for l in li:
    #             l = li if len(list) > 0 else ''
    #             # 将网址格式统一
    #             item = re.sub(r"//www.bilibili.com",'',l)
    #             content_list.append(item)
    #     return content_list

    def get_ps_tid(self,url):
        '''获取ps和tid的值'''
        html_str = self.parse_url(url)

        html_str = re.findall(r'=({.*});',html_str)
        html_str = html_str[0]
        # html_str = json.loads(html_str)
        fenlei_name = re.findall(r'"name":"(.*?)",',html_str)
        ps= re.findall(r'"ps":(\d+?),',html_str)
        tid= re.findall(r'"tid":(\d+?),',html_str)
        return fenlei_name,ps,tid

    def parse_url(self,url):
        '''发送请求，获取响应'''
        bl_html = requests.get(url, headers=self.headers).content.decode()
        return bl_html

    def get_xml(self,cid_list,fenlei_name):
        '''请求xml的url并保存弹幕'''
        for num in cid_list:    # 遍历cid列表，设置弹幕请求url
            # 接收弹幕的url，调用函数，发送请求，获取结果
            danmu_xlm = self.parse_url(self.danmu_url.format(num)).encode() # 解析时说有问题,获取结果是用encode()转为byte型
            # 将获取到的xml类型转换成etree对象
            xml_etree_obj = etree.HTML(danmu_xlm)
            # 获取弹幕列表
            l = xml_etree_obj.xpath('//d/text()')
            # 直接保存数据
            self.save_danmu(l,num,fenlei_name)

    def save_danmu(self,danmu_list,cid,fenlei_name):
        with open('哔哩哔哩爬取/{}/bilibili-{}.txt'.format(fenlei_name,cid), 'a', encoding='utf-8') as f:
            for danmu_str in danmu_list:
                f.write(danmu_str)
                f.write('\n')
        print('保存--{}--成功!'.format(cid))

    def run(self):
        # 1.获取视频的url
        fenlei_name_list, ps_list, tid_list= self.get_ps_tid(self.bili_url)
        fenlei_name_list.pop(1)
        ps_list.append('15')
        print(fenlei_name_list,ps_list,tid_list)
        # 每个大的分类
        for tid in tid_list:
            bl_html = self.parse_url(self.url.format(tid))
            print('使用正则获取aid')
            aid_list = re.findall(r'"aid":(\d+)', bl_html)
            # 大分类里面的视频
            for aid in aid_list:
                video_url = self.bili_video_url.format(aid)
                # 2.发送请求，获取数据
                bl_html = self.parse_url(video_url)
                # 3.提取数据
                print('使用正则获取cid')
                cid_list = re.findall(r'"cid":(\d+)',bl_html)
                print(cid_list)
                # 请求xml的url并保存弹幕
                self.get_xml(cid_list, fenlei_name_list[tid_list.index(tid)])




if __name__ == '__main__':
    bili = BiLi()
    bili.run()

# 动态里面
# https://api.bilibili.com/x/web-interface/dynamic/region?ps=15&rid=86
# https://api.bilibili.com/x/web-interface/dynamic/region?ps=15&rid=27
# 排名里面
# https://api.bilibili.com/x/web-interface/ranking/region?rid=27


