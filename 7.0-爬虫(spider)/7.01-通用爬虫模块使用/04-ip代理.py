# coding=utf-8

import requests

# 代理ip，HTTPS和HTTP必须对上，否则处407错误
proxies = {'http':'http://132.232.173.59:36328',
           'https':'https://132.232.173.59:36328',
           }

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

response = requests.get('http://www.baidu.com', proxies=proxies, headers=headers)
print(response.status_code)
