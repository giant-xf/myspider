# coding=utf-8

import requests
import base64
import random
session = requests.session()
headers = {
        'Accept' : 'application/json, text/javascript, */*; q=0.01',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep - alive',
        'Content - Length': '319',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'wap.yn.10086.cn',
        'Referer': 'http: // wap.yn.10086.cn / login.thtml',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'X - Requested - With': 'XMLHttpRequest',
    }
url = "http://wap.yn.10086.cn/actionDispatcher.do?ynrlpd=smsVerifyCode"
payload = {
    'reqUrl': 'smsVerifyCode',
    'smsType': '1',
    'mobile': '6821c74ffa9fa9e1bcbedbc4ec2c25755446b7b76edce501a122f9fe5b39776cbb4b532be596f7f32d2a40c9587b1c1ad986c93a00b51f527347d196ad5886b90bf25f53b6e63f2864072c5d0f08f969dc632fd849768ddd2ff1f3cc393fdcbbcb12ecf50dfc3847c25ba0ef9b8df836b3bf2a4ca7c93a5c8afdd0dc486921a3',
    'busiNum': 'LOGIN',
    'operType': '0'
}
r = session.post(url=url, data=payload)
print session.cookies
print r.text


url = 'http://wap.yn.10086.cn/actionDispatcher.do?ynrlpd=smsVerifyCode'
data = {
    'reqUrl': 'smsVerifyCode',
    'smsType': '1',
    'mobile': '6821c74ffa9fa9e1bcbedbc4ec2c25755446b7b76edce501a122f9fe5b39776cbb4b532be596f7f32d2a40c9587b1c1ad986c93a00b51f527347d196ad5886b90bf25f53b6e63f2864072c5d0f08f969dc632fd849768ddd2ff1f3cc393fdcbbcb12ecf50dfc3847c25ba0ef9b8df836b3bf2a4ca7c93a5c8afdd0dc486921a3',
    'busiNum': 'LOGIN',
    'operType': '0'
}
# url = 'http://wap.yn.10086.cn/resource/cloud/LOGIN2/html/login2VerifyCodeImage.jsp?t={}'.format(random.random())
res = requests.post(url,data=data)
print res.text
# 拼接cookies和设置cookies
# cookieJar = requests.cookies.RequestsCookieJar()
# for cookie in res.cookies:
#     cookieJar.set(cookie.name,cookie.value)
# cookieJar
#
#
# for cookie in res.headers['Set-Cookie'].split(";"):
#     key=cookie.split('=')[0]
#     value=cookie.split('=')[1]
#     cookieJar.set(key,value)

# print r.cookies
# print cookieJar








#
# r = session.get(url)
# # print session.headers
# # print session.cookies
# # print(r.content)
# with open(u'云南/yunnan.jpg', 'wb') as f:
#     f.write(r.content)
#
#
# url = 'http://wap.yn.10086.cn/actionDispatcher.do?ynrlpd=loginJt'
# data = {
#     'reqUrl': 'loginJt',
#     'funNum': 'sign',
#     'sign': '300011882721S0AB478G6B1Q6ATMM6SIN1NPF4D0OBKD20191103185358828G7M48AJ3DM9KD98QMKNT74IBL7QVB5461.0'
# }
# r = session.post(url, data=data)
# print r.text
#
# url = 'http://www.yn.10086.cn/service/actionDispatcher.do'
# payload = {
#     'reqUrl': 'login',
#     'busiNum': 'LOGIN',
#     'funNum': 'getPublicKey',
# }
# res = session.post(url, data=payload)
# print res.cookies
# # print res.content
# # res_json = res.json()
# # result_obj = res_json.get('resultObj') or {}
# # print result_obj

# headers = {
#         'Accept' : 'application/json, text/javascript, */*; q=0.01',
#         'Accept - Encoding': 'gzip, deflate',
#         'Accept - Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#         'Connection': 'keep - alive',
#         'Content - Length': '319',
#         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'Host': 'wap.yn.10086.cn',
#         'Referer': 'http: // wap.yn.10086.cn / login.thtml',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
#         'X - Requested - With': 'XMLHttpRequest',
#     }
# url = "http://wap.yn.10086.cn/actionDispatcher.do?ynrlpd=smsVerifyCode"
# payload = {
#     'reqUrl': 'smsVerifyCode',
#     'smsType': '1',
#     'phone': '8733c9bfb81656bab5161dfd15589bd43ff16d07ce5363742aa8d816f340a28308dca3e66778799e2f4a044a76cedafaae4d5c55fa795e9279b5ad68e49e70b5d83fbabf54777cc3e015ddf1b289be6408faa6ac27455d9aecd80bf487cb894598b52d75e3be8ce48d6a0b263cef95384aa0c37780d20543cdef2117262a4a0b',
#     'busiNum': 'LOGIN',
#     'operType': '0'
# }
# r = session.post(url=url, data=payload)
# print r.text



