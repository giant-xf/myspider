# coding = utf-8

import re
import requests
import json

class Neihan(object):
    '''内涵段子'''
    def __init__(self):
        self.url_temp = 'https://tieba.baidu.com/f?kw=%E6%AE%B5%E5%8F%8B%E4%B9%8B%E5%AE%B6&ie=utf-8&pn={}'
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def parse_url(self, url):
        '''解析url'''
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, content):
        '''提取数据'''
        p = re.compile(r"<div class=\"ti_title\">.*?<span>(.*?)</span>", re.S)
        content_list = p.findall(content)
        return  content_list

    def save_content_list(self, content_list):
        '''保存数据'''
        with open('内涵段子爬取/内涵段子.txt', 'w', encoding='utf-8') as f:
            for i in range(len(content_list)):
                for content in content_list[i]:
                    f.write(json.dumps(content, ensure_ascii=False))
                    f.write('\n')
                print('第%s页保存成功' % i)

    def run(self):
        num = 0
        list = []
        while num < 100:
            # 1.star_url
            url = self.url_temp.format(num)
            # 2.发送requests请求，获取响应
            html_str = self.parse_url(url)

            # 3.提取数据
            content_list = self.get_content_list(html_str)
            list.append(content_list)

            # 5.构造下一个请求链接
            num += 30
        # 4.保存数据
        self.save_content_list(list)
        print('保存完成')

if __name__ == '__main__':
    neihanduanzi = Neihan()
    neihanduanzi.run()








