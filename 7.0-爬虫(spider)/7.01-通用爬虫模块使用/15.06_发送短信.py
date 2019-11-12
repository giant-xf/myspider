# coding=utf-8

import requests

session = requests.session()

# 构造短信登录的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36nameAccount: 4008588180uid: 8378356736cb: JSONP_CALLBACK_10_24',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': '_n3fa_cid=4f901ec3e25d4f258e354774efdd4c3b; _n3fa_ext=ft=1571493854; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571493854; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571493865; unisecid=540BBB510A2FA39811872292BD3EF092',
    'Connection': 'keep-alive',
    'Host': 'uac.10010.com',
    'Referer': 'https://uac.10010.com/portal/homeLoginNew',
    'X-Requested-With': 'XMLHttpRequest',
}


# resp = session.get('https://uac.10010.com/portal/loadBanner?callback=jQuery17208717769497422292_1571494606934&_=1571494606952',headers=headers)
# print(resp.status_code)
# print(resp.content.decode())
#
# resp = session.get('https://uac.10010.com/portal/homeLoginNew')
# print(resp.status_code)
#
#
# resp = session.get('https://uac.10010.com/portal/Service/checkRelease?callback=jQuery17208717769497422292_1571494606935&_=1571494607201')
# print(resp.status_code)
# print(resp.content.decode())
#
# # mobile = input('请输入联通手机号:')
mobile = '16602735201'
#
# # https://uac.10010.com/portal/Service/CheckNeedVerify?callback=jQuery17207315229946823474_1571493864893&userName=17671451457&pwdType=02&_=1571493935975

# 检查是否需要发送验证码
check_need_verify_url = 'https://uac.10010.com/portal/Service/CheckNeedVerify'

check_need_verify_data ={
    'callback':'jQuery17207315229946823474_1571493864893',
    'userName': mobile,
    'pwdType':'02',
    '_':'1571493935975'
}

resp = session.get(check_need_verify_url, data=check_need_verify_data,headers=headers)
print(resp.status_code)
print(resp.content.decode())

# 发送验证码
verify_login_url = 'https://uac.10010.com/portal/Service/SendMSG'

verify_login_send_data = {
    'callback':'jQuery1720197331220240061_1571491230317',
    'req_time':'1571491285971',
    'mobile':mobile,
    '_':'1571491285972'
}

resp = session.get(verify_login_url, data=verify_login_send_data)
print(resp.status_code)
print(resp.content.decode())


# verify_login = 'https://uac.10010.com/portal/Service/MallLogin'
#
# verify_login_data = {
#             'callback': 'jQuery17206160369098513445_1571358605494',
#             'req_time': '1571358627742',
#             'redirectURL': 'http://www.10010.com',
#             'userName': mobile,
#             'password': input('请输入短信验证码'),
#             'pwdType': '02',
#             'productType': '01',
#             'redirectType': '01',
#             'rememberMe': '1',
#             '_': '1571358627743',
#         }
#
# resp = session.get(verify_login_url,data=verify_login_data)
# print(resp.status_code)
# print(resp.content.decode())


