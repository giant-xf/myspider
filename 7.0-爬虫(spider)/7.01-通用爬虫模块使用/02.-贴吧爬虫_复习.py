# coding=utf-8

import requests


class TiebaSpider(object):

    def __init__(self,spidername):
        self.spidername = spidername
        self.url = 'https://tieba.baidu.com/f?kw=' + spidername + '&ie=utf-8&pn={}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    def parse_url(self,url):
        # 发送请求，获取数据
        response = requests.get(url, headers=self.headers)
        html = response.content.decode()
        # html = response.text
        return html

    def run(self):
        # 1.构造url列表
        url_list = [ self.url.format(i*50) for i in range(1000)]

        # 2.遍历发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)

            print(html_str)

        # 3.保存数据

if __name__ == '__main__':
    tieba = TiebaSpider('李白')
    tieba.run()




