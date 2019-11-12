# coding=utf-8

import requests
from lxml import html

def gen_dict(text, prefix=''):
    root = html.fromstring(text)
    return dict(
        [(''.join(input.xpath('@name')),
          ''.join(input.xpath('@value'))) for input in root.xpath('{}//input'.format(prefix)) if input.xpath('@name') and input.xpath('@value')
         ])

session = requests.session()
url = 'https://wap.ha.10086.cn/login.action'
r = session.get(url)
data = gen_dict(r.text)
print data





