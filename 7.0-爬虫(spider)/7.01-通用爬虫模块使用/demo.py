# # coding=utf-8
#
import requests
import re
import json

# todo: 方法一, 使用session对象
#
# # 创建session对象
# session = requests.session()
#
# # 登录的地址
# post_url = 'http://www.renren.com/PLogin.do'
#
# # 账号密码打包成字典数据
# post_data = {'email': '13269764268', 'password': '88888888a'}
#
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}
#
# session.post(url=post_url, headers=headers, data=post_data)
#
# print(session.cookies.get_dict())
#
# response = session.get('http://www.renren.com/972184968/newsfeed/photo')
# html = response.content.decode()
# print(html)
# str = re.findall(r'李成家',html)
# print(str)

# todo:在headers中添加cookie
# session = requests.session()
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
#     'Cookie': 'anonymid=k08c658fi8jk5h; _r01_=1; jebe_key=cd78dc21-4d64-417c-b013-3701c998f99a%7C0db44f74a2dca345d4604ca9a98bfd4d%7C1567787600545%7C1%7C1567787603022; ln_uact=13269764268; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=cd78dc21-4d64-417c-b013-3701c998f99a%7C6ed4fe0e013c40f75b477aa3eb9e5677%7C1567841272092%7C1%7C1567841275002; _ga=GA1.2.1527801894.1567841807; _de=B9FE8FE7AAC97B95DE2F500122E863BC; depovince=GW; jebecookies=9faa3015-851b-40f2-91ad-0f5240f68d50|||||; JSESSIONID=abcG2cgaGPU_Aafg9-j3w; ick_login=6263f2f6-94d3-4a4a-af20-4c8e3fec0c6a; p=c1c442bc0756f6a486c5f389d63704d98; first_login_flag=1; t=456b874673490fc9eee4944e7c64fb928; societyguester=456b874673490fc9eee4944e7c64fb928; id=972184968; xnsid=35ffc684; ver=7.0; loginfrom=null; vip=1; wp_fold=0'
# }
#
# parse_url = 'http://www.renren.com/PLogin.do'
# response = session.get(url='http://www.renren.com/972184968/newsfeed/photo', headers=headers)
#
# html = response.content.decode()
# list = re.findall(r'李成家', html)
#
# print(list)

# todo:方法三
#
# headers = {
#      'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
#  }
#
# cookies = {"Cookies":'anonymid=k08c658fi8jk5h; _r01_=1; jebe_key=cd78dc21-4d64-417c-b013-3701c998f99a%7C0db44f74a2dca345d4604ca9a98bfd4d%7C1567787600545%7C1%7C1567787603022; ln_uact=13269764268; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=cd78dc21-4d64-417c-b013-3701c998f99a%7C6ed4fe0e013c40f75b477aa3eb9e5677%7C1567841272092%7C1%7C1567841275002; _ga=GA1.2.1527801894.1567841807; _de=B9FE8FE7AAC97B95DE2F500122E863BC; depovince=GW; jebecookies=9faa3015-851b-40f2-91ad-0f5240f68d50|||||; JSESSIONID=abcG2cgaGPU_Aafg9-j3w; ick_login=6263f2f6-94d3-4a4a-af20-4c8e3fec0c6a; p=c1c442bc0756f6a486c5f389d63704d98; first_login_flag=1; t=456b874673490fc9eee4944e7c64fb928; societyguester=456b874673490fc9eee4944e7c64fb928; id=972184968; xnsid=35ffc684; ver=7.0; loginfrom=null; vip=1; wp_fold=0'}
#
# cookies = { i.split('=')[0]:i.split('=')[1] for i in cookies['Cookies'].split(';')}
# print(cookies)
# # session = requests.session()
# #
# # response = session.get(url='http://www.renren.com/972184968/newsfeed/photo', headers=headers, cookies=cookies)
# #
# #
# # html = response.content.decode()
# # str = re.findall(r'李成家', html)
# # print(str)

# import calendar
# import time
#
# def get_year_month(n):
#     '''获取n个月前的年份和月份和天数'''
#     day_now = time.localtime()
#     year0 = day_now.tm_year
#     month0 = day_now.tm_mon
#
#     print(day_now,year0,month0)
#
#     monthx = month0 - n
#     yearx = year0
#     if monthx < 1:
#         yearx = year0 - n
#         monthx = month0 + 12 - n
#
#     day_begin = '%d%02d01' % (yearx, monthx)  # 月初肯定是1号
#     wday, monthRange = calendar.monthrange(yearx, monthx)  # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
#     day_end = '%d%02d%02d' % (yearx, monthx, monthRange)
#
#     day_begin2 = '%d-%02d-01' % (yearx, monthx)
#     day_end2 = '%d-%02d-%02d' % (yearx, monthx, monthRange)
#
#     return yearx, monthx, day_begin, day_end, monthRange, day_begin2, day_end2
#
#
# if __name__ == '__main__':
#     print(get_year_month(0))


# cookie ='JSESSIONID=946B39AE44B71D4C2402D93007099BD5; route=f6580975dacd2642305771459ba78210; e3route=c46ea420375f2b0dfa96a05e2c3e9a55281e236f; SHOP_PROV_CITY=; _n3fa_cid=25fbf85f7dd9409592268c365ad40d49; _n3fa_ext=ft=1571287597; tianjincity=11|110; tianjin_ip=0; u_mobilePhone=; u_psptId=; MUT=a2e40328-468f-4fe5-8355-3ad1c14074c2; USER_NAME=%E9%99%88%E9%9B%84%E5%B3%B0; mallchannel=06-0322-2383-9999; Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1571290568; Hm_lpvt_9208c8c641bfb0560ce7884c36938d9d=1571290568; UID=qGohrgz5Eh2k4MMzqJFQUXwZqRrFbTEU; MUT_V=null; backUrl=http://www.10010.com; loginType=06; WT_FPC=id=27c47e18af7a95065891571287580211:lv=1571295088862:ss=1571295088847; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571287597,1571290369,1571295112; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571295112; piw=%7B%22login_name%22%3A%22176****1457%22%2C%22nickName%22%3A%22%E9%99%88%E9%9B%84%E5%B3%B0%22%2C%22rme%22%3A%7B%22ac%22%3A%22%22%2C%22at%22%3A%22%22%2C%22pt%22%3A%2201%22%2C%22u%22%3A%2217671451457%22%7D%2C%22verifyState%22%3A%22%22%7D; _uop_id=56f7e1bcf1bbba64bdbca80807edeecd; userprocode=071; citycode=710; mallcity=71|710; loginflag=true; mallflag=null; JUT=LC95vyFOGdxY/7RKjR/eS+Gk6aT0puvNauTNcDTwwMDhpGTAtoavlZ6wu7XQHA9Nkh/xVEFz+vXrBhijJBhLUsgOmC9URptV0o7tQs9Ke1BJMO3v83uIKd6cePiXnSK3IFoef0bQ9v1wVxTeBS8TsvTmqhpEtPOkDsqZwt1c/4MCu3yxSBnaZNDzdYssBwAECwOhGI+aENk5Jg1HjEcIEwPnvkX2M3u7OLuNlHjqIVjJGlCxUM8JA2ZeahV9J9VVNobP8v1wyfOmTGrME3Slqc/Lg2JP9lZCwJMoSJ6/OtgUUJHxv9Thc5IHPcbN5HQbdtKeB9/PHUzTZAclG5//7fJmbcMsrZu7SFTeBZJf7E4UgCjVnudOKzJuc0tkZwETdaWT6MI3inL8w8hsO0dtmHJULLMD8+jEug5XObQszxIsMPXs3XAGASbKNhoIkEcAY+Hsqus3lTMzFyiyksEYJsywPzVyAe5uT9ZjvBxcBQTLWaQgsz9AZajygFwpoCBzAeqJf1azC2Q8bRQgWbrpLfU/vag+r87kGZBBzSa40rrsdRa5Tr8CdA==; security_session_verify=310d2e5359703501b1c39a7cc462ae46; MII=000100030001'
#
# cookies = {i.split('=')[0]: i.split("=")[1] for i in cookie.split('; ')}
#
#
# datax={
#     'pageNo': '1',
#     'pageSize': '40',
#     'beginDate': '20191001',
#     'endDate':'20191017',
# }
# url='https://iservice.10010.com/e3/static/query/callDetail?_=1571293178840&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html?_=1571290662589&menuid=000100030001'
#
# response = requests.post(url=url,headers=headers,data=datax,cookies=cookies)
#
# dict_str = json.loads(response.content.decode())
#
# result_list = dict_str['pageMap']['result']
#
# with open('联通.txt', 'w', encoding='utf-8') as f:
#     for i in result_list:
#         f.write(json.dumps(i,ensure_ascii=False))
#         f.write('\n')



import xlwt
import pandas as pd

def export_excel(data):
    # 将字典列表转换为DataFrame
    pf = pd.DataFrame(list(data))
    # 指定字段顺序
    order = [ key for key,value in data[0].items()]

    pf = pf[order]
    # 将列名替换为中文
    # columns_map = {
    #     'road_name': '路线',
    #     'bus_plate': '车牌',
    #     'timeline': '时间',
    #     'road_type': '方向',
    #     'site': '站点'
    # }
    # pf.rename(columns=columns_map, inplace=True)
    # 指定生成的Excel表格名称
    file_path = pd.ExcelWriter('联通通话记录.xlsx')
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()

cookie ='JSESSIONID=946B39AE44B71D4C2402D93007099BD5; route=f6580975dacd2642305771459ba78210; e3route=c46ea420375f2b0dfa96a05e2c3e9a55281e236f; SHOP_PROV_CITY=; _n3fa_cid=25fbf85f7dd9409592268c365ad40d49; _n3fa_ext=ft=1571287597; tianjincity=11|110; tianjin_ip=0; u_mobilePhone=; u_psptId=; MUT=a2e40328-468f-4fe5-8355-3ad1c14074c2; USER_NAME=%E9%99%88%E9%9B%84%E5%B3%B0; mallchannel=06-0322-2383-9999; Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1571290568; Hm_lpvt_9208c8c641bfb0560ce7884c36938d9d=1571290568; UID=qGohrgz5Eh2k4MMzqJFQUXwZqRrFbTEU; MUT_V=null; backUrl=http://www.10010.com; loginType=06; WT_FPC=id=27c47e18af7a95065891571287580211:lv=1571295088862:ss=1571295088847; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571287597,1571290369,1571295112; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571295112; piw=%7B%22login_name%22%3A%22176****1457%22%2C%22nickName%22%3A%22%E9%99%88%E9%9B%84%E5%B3%B0%22%2C%22rme%22%3A%7B%22ac%22%3A%22%22%2C%22at%22%3A%22%22%2C%22pt%22%3A%2201%22%2C%22u%22%3A%2217671451457%22%7D%2C%22verifyState%22%3A%22%22%7D; _uop_id=56f7e1bcf1bbba64bdbca80807edeecd; userprocode=071; citycode=710; mallcity=71|710; loginflag=true; mallflag=null; JUT=LC95vyFOGdxY/7RKjR/eS+Gk6aT0puvNauTNcDTwwMDhpGTAtoavlZ6wu7XQHA9Nkh/xVEFz+vXrBhijJBhLUsgOmC9URptV0o7tQs9Ke1BJMO3v83uIKd6cePiXnSK3IFoef0bQ9v1wVxTeBS8TsvTmqhpEtPOkDsqZwt1c/4MCu3yxSBnaZNDzdYssBwAECwOhGI+aENk5Jg1HjEcIEwPnvkX2M3u7OLuNlHjqIVjJGlCxUM8JA2ZeahV9J9VVNobP8v1wyfOmTGrME3Slqc/Lg2JP9lZCwJMoSJ6/OtgUUJHxv9Thc5IHPcbN5HQbdtKeB9/PHUzTZAclG5//7fJmbcMsrZu7SFTeBZJf7E4UgCjVnudOKzJuc0tkZwETdaWT6MI3inL8w8hsO0dtmHJULLMD8+jEug5XObQszxIsMPXs3XAGASbKNhoIkEcAY+Hsqus3lTMzFyiyksEYJsywPzVyAe5uT9ZjvBxcBQTLWaQgsz9AZajygFwpoCBzAeqJf1azC2Q8bRQgWbrpLfU/vag+r87kGZBBzSa40rrsdRa5Tr8CdA==; security_session_verify=310d2e5359703501b1c39a7cc462ae46; MII=000100030001'

cookies = {i.split('=')[0]: i.split("=")[1] for i in cookie.split('; ')}

datax={
    'pageNo': '1',
    'pageSize': '40',
    'beginDate': '20191001',
    'endDate':'20191017',
}
url='https://iservice.10010.com/e3/static/query/callDetail?_=1571293178840&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html?_=1571290662589&menuid=000100030001'

response = requests.post(url=url,headers=headers,data=datax,cookies=cookies)

dict_str = json.loads(response.content.decode())

result_list = dict_str['pageMap']['result']

print(result_list)
export_excel(result_list)

# with open('aa.xls','w') as f:
#     f.write(str(result_list))

# from pandas import DataFrame as DF
# df = DF(result_list)
# df.to_csv('联通通讯记录.xls')



