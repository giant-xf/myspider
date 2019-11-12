# coding=utf-8

import requests


class TiebaSpider(object):
    '''爬取贴吧类容'''

    def __init__(self, spidername):
        self.spidername = spidername
        self.url = 'https://tieba.baidu.com/f?kw=' + spidername + '&ie=utf-8&pn={}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    def get_url_list(self):
        # 1.构造url列表
        # url_list = []
        # for i in range(10000):
        #     url_list.append(self.url.format(i*50))
        # return url_list

        return [self.url.format(i * 50) for i in range(10000)]

    def parse_url(self, url):
        # 2.遍历，发送请求，获取响应
        response = requests.get(url, headers=self.headers)
        html_str = response.content.decode()
        return html_str

    def save_html(self, html_str, page_num):
        # 3.保存html字符串
        html_path = './贴吧爬取/{}-第{}页.html'.format(self.spidername, page_num)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_str)

    def run(self):
        # 1.构造url列表
        url_list = self.get_url_list()

        # 2.遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)

            # 获取循环的次数
            page_num = url_list.index(url) + 1
            # 3.保存
            self.save_html(html_str, page_num)
            print('第%s页保存成功!!' % page_num)


if __name__ == '__main__':
    spidername = input('请输入需要爬取的页面:')
    t = TiebaSpider(spidername)
    t.run()
