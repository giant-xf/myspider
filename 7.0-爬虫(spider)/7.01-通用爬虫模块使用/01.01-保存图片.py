

import requests
import json
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
proxies = {'http':'http://132.232.173.59:36328',
           'https':'https://132.232.173.59:36328',
           }

with open('贴吧爬取每个帖子图片/赵丽颖.txt','r',encoding='utf-8') as f:
    content_list = f.readlines()[0]
    print(content_list)
    content_list = json.loads(content_list)
    # 保存图片
    for img_url in content_list['img_list']:
        print(img_url)
        not_list=["http://aod-image.baidu.com/5/pic/38e2824ec9e42dcd705a0f5b375ae839.jpg","http://aod-image.baidu.com/0/pic/c1feddc63eb397bdd23ce58731d732dd.jpg","http://aod-image.baidu.com/0/pic/2ae9525064c96c5770e45db0fb9ef13c.jpg"]
        if img_url not in not_list:
            print(img_url)
            url_response = requests.get(img_url, headers=headers, proxies=proxies)
            file_name1='贴吧爬取每个帖子图片/'+re.findall(r'sign=.*/(.*)',img_url)[0]
            with open(file_name1, "wb") as f:
                f.write(url_response.content)
            print('保存成功')





