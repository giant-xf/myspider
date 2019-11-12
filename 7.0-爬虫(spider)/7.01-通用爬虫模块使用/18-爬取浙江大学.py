# coding=utf-8

import requests
import re
import json
import time
import hashlib
from lxml import etree

session = requests.session()

'''
/api/front/index/curr/themelangcn
/api/front/codes/key/subject/codescodetype3langcn
/api/front/psons/searchlangcnpage0size12
'''



# timestamp = '1573036443000'
# '1f11192bd9d14a09b29fc59d556e24e3/api/front/index/curr/themelangcn1573035145000 1f11192bd9d14a09b29fc59d556e24e3'
path1 = '/api/front/index/curr/themelangcn'
path2 = '/api/front/codes/key/subject/codescodetype3langcn'
path3 = '/api/front/psons/searchlangcnpage0size12'
def encode_sign(path):
    e = '1f11192bd9d14a09b29fc59d556e24e3'
    timestamp = str(int(time.time()) * 1000)
    # lang = 'langcn'
    s = e+path+timestamp+' '+ e

    sign = hashlib.md5(s.encode(encoding='UTF-8')).hexdigest()
    return sign,timestamp

sign, timestamp = encode_sign(path2)
headers = {
    'appKey': '50634610756a4c0e82d5a13bb692e257',
    'sign':sign,
    'timestamp': timestamp,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

# 教师分类请求url
cate_url = 'https://person.zju.edu.cn/server/api/front/codes/key/subject/codes?codetype=3&lang=cn'


cate_str = requests.get(cate_url, headers=headers)
print(cate_str.status_code)
# print cate_str.text

cate_list =cate_str.json()['data']['content']

cate_dict = {cate['codekey']:cate['codename'] for cate in cate_list }
print(cate_dict)


for codekey,cadename in cate_dict.items():
    print(codekey)
    # 请求教师列表
    sign, timestamp = encode_sign(path3)
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'appKey': '50634610756a4c0e82d5a13bb692e257',
        'Connection': 'keep-alive',
        'Host': 'person.zju.edu.cn',
        'Referer': 'https://person.zju.edu.cn/index/search',
        'sign': sign,
        'timestamp': timestamp,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    # 教师列表请求url
    teacher_list_url = 'https://person.zju.edu.cn/server/api/front/psons/search?subjects={}&size=12&page=0&lang=cn'.format(codekey)

    teacher_resp = requests.get(teacher_list_url)
    print(teacher_resp.status_code)
    # 教师信息列表字典[{}{}{}{}]
    print(teacher_resp.content.decode())
    teacher_list = json.loads(teacher_resp.content.decode())['data']['content']
    # 存放老师信息
    content = {}
    content['cadename'] = cadename
    for teacher in teacher_list:
        content['cn_name'] = teacher['cn_name']
        content['college_name'] = teacher['college_name']
        content['mapping_name'] = teacher['mapping_name']
        content['work_post'] = teacher['work_post']
        content['work_title'] = teacher['work_title']
        content['work_title_name'] = teacher['work_title_name']
        headers1 = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'appKey': '50634610756a4c0e82d5a13bb692e257',
            'Connection': 'keep-alive',
            'Cookie': 'Hm_lvt_fe30bbc1ee45421ec1679d1b8d8f8453=1571223832,1571272835,1571273009,1571577852; Hm_lpvt_fe30bbc1ee45421ec1679d1b8d8f8453=1571577852; route=2213d1f7ae0c2524e32446b9b771428c; JSESSIONID=CDC1398AACCDFAA8ABB3285B690B21D3; BSFIT_EXPIRATION=1571638105341; BSFIT_DEVICEID=es-fKCv4HwRTht8gFRPgHHZtk_jTAIw89i7e-EBYIP42xbaFI5eNNdZlzHnePT_2v-GqpRDMxss47-tii21Gm1KN9AP5exBHFDjrFcCA3WTjcwpZYqFolg3mNpKO8aOjE0wqY2ZlYplTAVRihSlPNtd_iq1eGPXz; wsess=9q33f6t0m2pukhfll54j5r7e70; _pk_ref.1.f8a7=%5B%22%22%2C%22%22%2C1571579859%2C%22http%3A%2F%2Fwww.zju.edu.cn%2F%22%5D; _pk_id.1.f8a7=0c9c6e752f4a72a9.1571206106.6.1571579859.1571579859.; _pk_ses.1.f8a7=1; BSFIT_h/q57=KvRMKvRM6vdIKvQaKd,K5h0pa+wK5KMpd,K5hXp5hwK52MKd,K5h06v2wK5K06+',
            'Host': 'person.zju.edu.cn',
            'Referer': 'https://person.zju.edu.cn/index/search',
            'Upgrade - Insecure - Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        teacher_detail_url = 'https://person.zju.edu.cn/{}'.format(content['mapping_name'])
        html_str = requests.get(teacher_detail_url,headers=headers1).text
        html = etree.HTML(html_str)
        # html_str = re.findall(r'')

        personal_img = html.xpath("//div[@class='baseInfo']/div[@class='personal_img']/img/@src")
        content['personal_img'] = personal_img[0] if len(personal_img)>0 else None

        telephone = html.xpath("//div[ @class ='baseInfo']//li[@ class ='telephone'] / text()")
        content['telephone'] = telephone[0] if len(telephone)>0 else None

        email = html.xpath("//div[ @class ='baseInfo']//li[@ class ='email'] / text()")
        content['email'] = email[0] if len(email)>0 else None

        address = html.xpath("//div[ @class ='baseInfo']//li[@ class ='address'] / text()")
        content['address'] = address[0] if len(address)>0 else None

        with open('浙江大学.txt', 'a+', encoding='gbk') as f:
            f.write(json.dumps(content, ensure_ascii=False, indent=3))

    print('{}保存完成'.format(content['cadename']))

print('全部保存完成')

