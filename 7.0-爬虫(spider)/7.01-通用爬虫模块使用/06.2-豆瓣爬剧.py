# coding=utf-8

import urllib3

urllib3.disable_warnings()

import requests
import json
from urllib import parse


class DoubanSpider(object):
    def __init__(self):
        self.url_temp_list = [
            'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start={}',
            'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}',
            'https://movie.douban.com/j/search_subjects?type=tv&tag=%E9%9F%A9%E5%89%A7&sort=recommend&page_limit=20&page_start={}',
            'https://movie.douban.com/j/search_subjects?type=tv&tag=%E6%B8%AF%E5%89%A7&sort=recommend&page_limit=20&page_start={}',
            'https://movie.douban.com/j/search_subjects?type=tv&tag=%E6%97%A5%E6%9C%AC%E5%8A%A8%E7%94%BB&sort=recommend&page_limit=20&page_start={}'
        ]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        self.content_list = []

    def parse_url(self, url):
        '''发送请求'''
        response = requests.get(url, headers=self.headers)
        print('状态码:', response.status_code)
        return response.content.decode()

    def get_content_list(self, json_str):
        '''提取数据'''
        # 将json字符串转换成python字典
        dict_ret = json.loads(json_str)
        content_list = dict_ret['subjects']
        return content_list

    def save_content_list(self, content_list):
        '''保存数据'''
        with open('豆瓣爬虫/douban.txt', 'w', encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=3))
                f.write('\n')

    def run(self):
        for url_temp in self.url_temp_list:
            # 获取电视剧的类型
            tv_name = parse.unquote(url_temp.split('&')[1].split('=')[1]) + ':'
            print('开始获取%s' % tv_name)
            self.content_list.append(tv_name)
            num = 0
            while True:
                # 1.star_url
                url = url_temp.format(num)
                # 2.发送请求
                json_str = self.parse_url(url)
                # 3.提取数据
                self.content_list.append(self.get_content_list(json_str))

                # 退出循环的条件
                if len(self.content_list) < 20:
                    break

                # 5.构造下一个请求的url地址
                num += 20
                # 4.保存数据
        self.save_content_list(self.content_list)
        print('保存完成')


if __name__ == '__main__':
    doubanspider = DoubanSpider()
    doubanspider.run()
