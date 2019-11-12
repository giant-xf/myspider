# coding=utf-8
import requests
from lxml import html

headers = {
    "Cookie": "AlteonP=FE8rOXcYYAohtwg0A+3mLA$$; mobileNo=13837470397; JSESSIONID=0000bQBYpREbAZ7a9-G01WxQEjb:-1; kddatekey=kddate; channelheader=; 4GgetNums=1; CmLocation=270|270; CmProvid=hb; mobile=5232-41879-4959-33662; WT_FPC=id=2ea572c6f5c97c474e21573459211574:lv=1573461595686:ss=1573459211574"
}
# url = 'http://wap.ha.10086.cn/person/user-info.action?menuCode=61054'
# r = requests.get(url,headers=headers)
# print (r.text)
# r_html = html.fromstring(r.text)
# info_list = r_html.xpath('//div[@class="text"]/p/text()')
# print (info_list)
#
# for _ in info_list:
#     _ = _.replace('\r', '').replace('\t', '').replace('\n','')
#     if u'机主姓名：' in _:
#         print(_.replace(u'机主姓名：',' '))
#     elif u'手机号码：' in _:
#         print(_.replace(u'手机号码：',' '))
#     elif u'地市归属：' in _:
#         print(_.replace(u'地市归属：',' '))
#     elif u'入网时间：' in _:
#         print(_.replace(u'入网时间：',' '))
#     elif u'实名状态：' in _:
#         print(_.replace(u'实名状态：',' '))
import re
# url = 'http://wap.ha.10086.cn/service-index.action?type=check'
# r = requests.get(url,headers=headers)
# print r.text
# # balance = re.compile(ur'账户余额：.+?>(.+?)<').findall(r.text)[0]
# #
# # print balance

url = 'http://wap.ha.10086.cn/fee/query-month-account.action?menuCode=61043&billingCycless={}&billingCycle={}'
month_list =  ['201911', '201910', '201909', '201908', '201907', '201906']

r = requests.get(url.format('1','201910'),headers=headers)
print r.text
costs = re.compile(ur'<span class="money"><b> (.+?) <').findall(r.text)
print costs
# for month in month_list:
#     url = url.format(month_list.index(month),month)
#     res = requests.get(url,headers=headers)
#     costs = re.compile(ur'<span class="money"><b> (.+?) <').findall(res.text)
#     print costs