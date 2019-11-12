# coding=utf-8

import requests

# todo: 方法一, 使用session对象

# 创建一个session对象
session = requests.session()

# 登录的地址
post_url = 'http://www.renren.com/PLogin.do'

# 账号密码打包成字典数据
post_data = {'email': '13269764268', 'password': '88888888a'}

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

# 将登录的cookie信息保存到session中
session.post(post_url, headers=headers, data=post_data)
print(session.cookies.get_dict())
# 利用session发送get请求
response = session.get('http://www.renren.com/972184968/newsfeed/photo', headers=headers)

with open('renren.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode())

print(response.status_code)


# todo: 方法二， 直接在headers中加入cookie
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Cookie': 'anonymid=k08c658fi8jk5h; depovince=GW; _r01_=1; JSESSIONID=abcerh9TCU79HeRVGAh0w; ick_login=a84783dc-8f19-43a8-a5a8-8e5017aab006; jebe_key=cd78dc21-4d64-417c-b013-3701c998f99a%7C0db44f74a2dca345d4604ca9a98bfd4d%7C1567787600545%7C1%7C1567787603022; XNESSESSIONID=9aef001f3fc4; ick=bdae76df-42a3-4c69-a3aa-4c4392b4f292; wp_fold=0; jebecookies=091c0b42-215e-4ebe-b4f8-185508545e5b|||||; _de=B9FE8FE7AAC97B95DE2F500122E863BC; p=a078c6086c15814e464f6c59e0b3e4c08; first_login_flag=1; ln_uact=13269764268; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=e542ad96c6d968f1c0e4e2477cf364878; societyguester=e542ad96c6d968f1c0e4e2477cf364878; id=972184968; xnsid=f8870baf; ver=7.0; loginfrom=null; jebe_key=cd78dc21-4d64-417c-b013-3701c998f99a%7C6ed4fe0e013c40f75b477aa3eb9e5677%7C1567789230524%7C1%7C1567789233003'
}

response = requests.get('http://www.renren.com/972184968/newsfeed/photo', headers=headers)

with open('renren1.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode())

print(response.status_code)
'''
# todo: 方法三, 在请求中添加cookie参数

# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
# }
#
# cookies = 'anonymid=k08c658fi8jk5h; _r01_=1; jebe_key=cd78dc21-4d64-417c-b013-3701c998f99a%7C0db44f74a2dca345d4604ca9a98bfd4d%7C1567787600545%7C1%7C1567787603022; ln_uact=13269764268; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=cd78dc21-4d64-417c-b013-3701c998f99a%7C6ed4fe0e013c40f75b477aa3eb9e5677%7C1567841272092%7C1%7C1567841275002; _ga=GA1.2.1527801894.1567841807; depovince=GW; jebecookies=4ba19717-2783-459e-a39c-ff449330338c|||||; JSESSIONID=abcRy2_YMj_Qr6sh3Kz1w; ick_login=f09d5059-8c4a-426d-92c6-d69ad6df9232; _de=B9FE8FE7AAC97B95DE2F500122E863BC; p=7c1430c1cd8fd3b0b6688a99920a84e58; first_login_flag=1; t=2e04c016c819f112a4747afbcea907f68; societyguester=2e04c016c819f112a4747afbcea907f68; id=972184968; xnsid=a66af7c7; ver=7.0; loginfrom=null; wp_fold=0'
# # 将cookies转换成字典
# cookies = {i.split('=')[0]: i.split("=")[1] for i in cookies.split('; ')}
#
# response = requests.get('http://www.renren.com/972184968/newsfeed/photo', headers=headers, cookies=cookies)
#
# with open('renren2.html', 'w', encoding='utf-8') as f:
#     f.write(response.content.decode())
#
# print(response.content.decode())





