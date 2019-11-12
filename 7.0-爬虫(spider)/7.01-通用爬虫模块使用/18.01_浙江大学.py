# coding=utf-8
import requests
import json

# headers = {
#     'Accept':'application/json, text/plain, */*',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'appKey': '50634610756a4c0e82d5a13bb692e257',
#     'Connection': 'keep-alive',
#     'Cookie': 'route=2213d1f7ae0c2524e32446b9b771428c; JSESSIONID=CDC1398AACCDFAA8ABB3285B690B21D3; BSFIT_EXPIRATION=1571638105341; BSFIT_DEVICEID=es-fKCv4HwRTht8gFRPgHHZtk_jTAIw89i7e-EBYIP42xbaFI5eNNdZlzHnePT_2v-GqpRDMxss47-tii21Gm1KN9AP5exBHFDjrFcCA3WTjcwpZYqFolg3mNpKO8aOjE0wqY2ZlYplTAVRihSlPNtd_iq1eGPXz; wsess=9q33f6t0m2pukhfll54j5r7e70; _pk_ref.1.f8a7=%5B%22%22%2C%22%22%2C1571579859%2C%22http%3A%2F%2Fwww.zju.edu.cn%2F%22%5D; _pk_ses.1.f8a7=1; Hm_lvt_fe30bbc1ee45421ec1679d1b8d8f8453=1571273009,1571577852,1571581326,1571585145; Hm_lpvt_fe30bbc1ee45421ec1679d1b8d8f8453=1571585145; _pk_id.1.f8a7=0c9c6e752f4a72a9.1571206106.6.1571585151.1571579859.; BSFIT_h/q57=KvRMKvR4pv7IKv+wKh,K5h465cwK5KwKh',
#     'Host': 'person.zju.edu.cn',
#     'Referer': 'https://person.zju.edu.cn/index/search',
#     'sign': 'e572948e94b38d496e550c3d381543f9',
#     'timestamp': '1571585242000',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
#     }
#
# # 教师列表请求url
# teacher_list_url = 'https://person.zju.edu.cn/server/api/front/psons/search?subjects=08&size=12&page=0&lang=cn'
# teacher_resp = requests.get(teacher_list_url,headers=headers)
# print(teacher_resp.status_code)
# print(teacher_resp.content.decode())
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
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
teacher_detail_url = 'https://person.zju.edu.cn/zhengqiang'
html_str = requests.get(teacher_detail_url,headers=headers1).text

print(html_str)

