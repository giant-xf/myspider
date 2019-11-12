# coding=utf-8

import requests
from lxml import html

headers = {
    "Cookie": "BIGipServerPOOL-XINWAP-8082=!15XmOakFHqbsWSttKjT8BkgYaAdSArV77QcWydjUjCZk75srw+hcDf/zmec6WmAO8U/t5lbOqzSxng==; cookiesession1=3025D903GYS9BCQMUQEI52LYBQMB8C66; TY_SESSION_ID=510845f3-ee97-433f-b4a6-31df9ac668c5; pageID_esPageUserLog=F61A7218824280B6C4732284CF6E57D4; wap_roteServer=PRODUCT; JSESSIONIDSHOPPING_NEW=3S6LHSZuKW2RrfebZm21H870XooczUt8pjGFQHAfOOr2tHbtr7CH!1745331199; URL_FROM_COOKIE_H5=H5; CmWebtokenid=13933967644,he; U_C_VS=7A8AB3710110DAC7D2EA1444AA635403D2B4D71AEF74034AAB39B1B421EBFB3E; wap_newb=4a19828b50720e8d4b27e6dd2549a732|1573457604|1573456459; WT_FPC=id=204bc68358b13c0dfec1573452601733:lv=1573457626319:ss=1573456469346"
}

url = 'http://wap.he.10086.cn/touch/queryServe!personInfo.action'

r = requests.get(url, headers=headers)
r_html = html.fromstring(r.text)
info_list = r_html.xpath('//p[@class="info"]/text()')
print (info_list)
for _ in info_list:
    if '13956565656'[:3] in _:
        print _.split(' ')[0]
    elif u'入网时间：' in _:
        in_net_date = _.replace(u'入网时间：', '')  # 2017-07-19 08:51:34
        print in_net_date
    elif u'证件号码：' in _:
        print _.replace(u'证件号码：', '')
    elif u'家庭住址：' in _:
        print _.replace(u'家庭住址：', '')




