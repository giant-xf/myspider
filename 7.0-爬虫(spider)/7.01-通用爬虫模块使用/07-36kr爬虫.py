# coding = utf-8

import re
import json
from parse_url import parse_url

url = 'https://36kr.com/'

html_str = parse_url(url)

ret = re.findall('<script>window.initialState=(.*?)</script>', html_str)[0]

with open('36kr爬取/36kr数据.json', 'w', encoding='utf-8') as f:
    f.write(ret)

ret = json.loads(ret)
print(ret)




