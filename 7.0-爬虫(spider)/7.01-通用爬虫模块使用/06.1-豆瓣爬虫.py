
# coding = utf-8

import urllib3

urllib3.disable_warnings()

import requests
import json
import re
from  parse_url import parse_url


proxies = {'http':'http://110.86.137.0:9999','https':'http://110.86.137.0:9999'}
ex_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag={}&page_limit=1000&page_start=0'

url = 'https://movie.douban.com/j/search_tags?type=movie&source=index'

response_dict = json.loads(parse_url(url))

move_name_list = response_dict["tags"]
print(move_name_list)

url_list = [ex_url.format(i) for i in move_name_list]

print(url_list)


for url in url_list:

    html_str = parse_url(url)
    print(html_str)
    # 将json数据转换成python数据
    response = json.loads(html_str)
    print(re.findall(r'tag=(.*?)&',url))
    # 存储数据
    dict = {}
    dict['类别'] = re.findall(r'tag=(.*?)&',url)
    list = []
    for i in range(10):
        title = response["subjects"][i]["title"]
        url = response["subjects"][i]["url"]
        rate = response["subjects"][i]["rate"]
        image = response["subjects"][i]["cover"]
        list.append({
            '片名':title,
            '播放地址':url,
            '豆瓣评分':rate,
            '封面':image
        })
    dict['电影集合'] = list

    with open('豆瓣爬虫/豆瓣电影.txt', 'a+', encoding='utf-8') as f:
        # ensure_ascii：关闭ASCII编码, indent: 缩进，使格式更加好看
        # for contents in dict:
        f.write(json.dumps(dict, ensure_ascii=False, indent=3))
        f.write('\n')
    print('保存完成')


    # with open('豆瓣爬虫/豆瓣网页.json', 'w', encoding='utf-8') as f:
    #     # f.write(json.dumps(response,ensure_ascii=False, indent=2))
    #     f.write()

    # print(response)


















