# coding=utf-8
import requests
import json
import time
import random
from selenium import webdriver
import xlwt
import pandas as pd


# 代理ip接口
# targetUrl = "http://test.abuyun.com/proxy.php"
#
# proxyHost = "http-pro.abuyun.com"
# proxyPort = "9010"
#
# proxyUser = "HY9B112923043QRP"
# proxyPass = "12310F98FC7A4367"
#
#
# proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
#     "host" : proxyHost,
#     "port" : proxyPort,
#     "user" : proxyUser,
#     "pass" : proxyPass,
# }
#
# proxies = {
#     "http"  : proxyMeta,
#     "https" : proxyMeta,
# }
#
# resp = requests.get(url=targetUrl,proxies=proxies)
#
# print(resp.status_code)

#
# option = webdriver.ChromeOptions()
# option.binary_location=r'D:\谷歌浏览器\Google\Chrome\Application\chrome.exe'
# #实例化driver
# chrome_driver = r"D:\workon_home\spider_py3\selenium\webdriver\chrome\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver,chrome_options=option)


session = requests.session()

def export_excel(data):
    '''
    保存到Excel格式
    :param data: 
    :return: 
    '''
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

# 构造登录的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36nameAccount: 4008588180uid: 8378356736cb: JSONP_CALLBACK_10_24',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': 'JSESSIONID=9FC759A807DFDA900E7A8A1D8B67C6BB; route=f6580975dacd2642305771459ba78210; SHOP_PROV_CITY=; _n3fa_cid=25fbf85f7dd9409592268c365ad40d49; _n3fa_ext=ft=1571287597; tianjincity=11|110; tianjin_ip=0; u_mobilePhone=; u_psptId=; MUT=a2e40328-468f-4fe5-8355-3ad1c14074c2; USER_NAME=%E9%99%88%E9%9B%84%E5%B3%B0; mallchannel=06-0322-2383-9999; Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1571290568; UID=qGohrgz5Eh2k4MMzqJFQUXwZqRrFbTEU; MUT_V=null; backUrl=http://www.10010.com; loginType=06; e3route=09238ba1d70493fb437b8757b88c17f9ada60744; Hm_lpvt_9208c8c641bfb0560ce7884c36938d9d=1571358556; _ga=GA1.2.1024364920.1571358557; _gid=GA1.2.56675778.1571358557; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571295112,1571302536,1571358605,1571368985; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571368985; piw=%7B%22login_name%22%3A%22176****1457%22%2C%22nickName%22%3A%22%E9%99%88%E9%9B%84%E5%B3%B0%22%2C%22rme%22%3A%7B%22ac%22%3A%22%22%2C%22at%22%3A%22%22%2C%22pt%22%3A%2201%22%2C%22u%22%3A%2217671451457%22%7D%2C%22verifyState%22%3A%22%22%7D; mallcity=71|710; citycode=710; userprocode=071; WT_FPC=id=27c47e18af7a95065891571287580211:lv=1571369092033:ss=1571368978087; mallflag=null; JUT=k7I/hPnOUYgDTlhjKZ9IBdB/IgMZrWWdscQg+XtqjhXPVJ8Lq9N0MqEApKSfr6W258/llOeg2ljBOIpvpyoNcWAP4GTd8JsE1Io1U3zswYM4xF3IcZ7BsG7EKFEnoRi7u80V70xKQh2i4EKzsYWZW6lHCFqfEYszJahNpTB4tERKGXrJIS4t6NPO7O3Bqni27OALJRM+YmKsl0VlFIA6kkTMAv+xWvDVZqY8oHW2cruCJ9O/4iI2L6xbRPAehdiVYxzBQk/Lzjmo+Mfi619bsS99fcLbPY9B42hG/z86SpleY096TNPEHT2wTH5rVfCdZToeOXwfBG/jHYIqCgvfZah6xw6kH0Vf7MIXzD3KzrIUVgbBOf45NtqseZxZ/z6/+yWr2Ton6jmJcO31EmxPEKNhDLySb0x2COardWOCdJNlXz6i1/Nbh9Bx+mG3dMf36XrJXc0yoHH3/sPJFYVVJLnA8Kg0HS8RuP9oZ+Z3AXdDiG+Ao8yxuwlSFwklW9PYyt87BtjB0sCFc1RBXaCylAcXg+UOpFNa0v4L559Kbg4=j5S9nxmFJ+KFN/yiUMTlgw==; _uop_id=f644e6df867314b39a5717496fd542e9; loginflag=true; MII=000100030001; security_session_verify=9f2b0cd6a88f31de2b0ae9ac8a1d995b',
    'Connection': 'keep-alive',
    'Host': 'uac.10010.com',
    'Referer': 'https://uac.10010.com/portal/homeLoginNew',
    'X-Requested-With': 'XMLHttpRequest',

}


# 生成随机数，构造时间
req_time = str(int(time.time()*1000))
# https://uac.10010.com/portal/Service/CheckNeedVerify?callback=jQuery17206942476292032751_1571314357805&userName=17617451457&pwdType=01&_=1571314375614
num = str(random.randint(100000,999999))
# print(num)
times = str(int(time.time()*1000))
# print(time)
# callback = 'jQuery17201636644500{}_{}'.format( num, str(int(time.time()*1000))),
callback='jQuery17206942476293332751{}_{}'.format(num, times)
print(callback)

# https://uac.10010.com/portal/Service/CheckNeedVerify?callback=jQuery17209082767106950329_1571324845031&userName=17671451457&pwdType=01&_=1571324927369

# 登录的请求体构造
login_data = {
    'callback':'jQuery17206160369098513445_1571358605494',
    'req_time': '1571358627742',
    'redirectURL':'http://www.10010.com',
    'userName':'17671451457',
    'password':'55555',
    'pwdType':'01',
    'productType':'01',
    'redirectType':'01',
    'rememberMe':'1',
    '_': '1571358627743',
    }

# print(login_data)

# https://uac.10010.com/portal/Service/SendMSG?callback=jQuery17201636644500591098_1571314439506
# &req_time=1571314454907
# &mobile=13047581370
# &_=1571314454908
# 设置callback随机值

# 设置callback随机值
callback = 'jQuery17201636644500592022_'+str(int(time.time()*1000))
# print(callback)

# 发送短信地址调用
send_data = {
    'callback':'jQuery17206160369098513445_1571358605494',
    'req_time':'1571358627742',
    'mobile':'17671451457',
    '_':'1571358627743',
}

# 登录的地址接口
login_url = 'https://uac.10010.com/portal/Service/MallLogin'
# 发送短信接口
send_url = 'https://uac.10010.com/portal/Service/SendCkMSG'

# 测试短信登录和账号密码登录
# response = requests.get(url=send_url,headers=headers,params=send_data)
# print(response.content.decode())

# rep = requests.get(url=send_url,headers=headers,params=send_data)

# rep = session.get(url=login_url,headers=headers,params=login_data)
# print(rep.status_code)
# print(rep.content.decode())

# print(session.cookies.get_dict())

# cookies = session.cookies.get_dict()

# driver.add_cookie(cookies)
# driver.get('https://iservice.10010.com/e4/query/bill/call_dan-iframe.html')

# 构造cookie
cookie ='JSESSIONID=9FC759A807DFDA900E7A8A1D8B67C6BB; route=f6580975dacd2642305771459ba78210; SHOP_PROV_CITY=; _n3fa_cid=25fbf85f7dd9409592268c365ad40d49; _n3fa_ext=ft=1571287597; tianjincity=11|110; tianjin_ip=0; u_mobilePhone=; u_psptId=; MUT=a2e40328-468f-4fe5-8355-3ad1c14074c2; USER_NAME=%E9%99%88%E9%9B%84%E5%B3%B0; mallchannel=06-0322-2383-9999; Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1571290568; UID=qGohrgz5Eh2k4MMzqJFQUXwZqRrFbTEU; MUT_V=null; backUrl=http://www.10010.com; loginType=06; e3route=09238ba1d70493fb437b8757b88c17f9ada60744; Hm_lpvt_9208c8c641bfb0560ce7884c36938d9d=1571358556; _ga=GA1.2.1024364920.1571358557; _gid=GA1.2.56675778.1571358557; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571295112,1571302536,1571358605,1571368985; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571368985; piw=%7B%22login_name%22%3A%22176****1457%22%2C%22nickName%22%3A%22%E9%99%88%E9%9B%84%E5%B3%B0%22%2C%22rme%22%3A%7B%22ac%22%3A%22%22%2C%22at%22%3A%22%22%2C%22pt%22%3A%2201%22%2C%22u%22%3A%2217671451457%22%7D%2C%22verifyState%22%3A%22%22%7D; mallcity=71|710; citycode=710; userprocode=071; WT_FPC=id=27c47e18af7a95065891571287580211:lv=1571369092033:ss=1571368978087; mallflag=null; JUT=k7I/hPnOUYgDTlhjKZ9IBdB/IgMZrWWdscQg+XtqjhXPVJ8Lq9N0MqEApKSfr6W258/llOeg2ljBOIpvpyoNcWAP4GTd8JsE1Io1U3zswYM4xF3IcZ7BsG7EKFEnoRi7u80V70xKQh2i4EKzsYWZW6lHCFqfEYszJahNpTB4tERKGXrJIS4t6NPO7O3Bqni27OALJRM+YmKsl0VlFIA6kkTMAv+xWvDVZqY8oHW2cruCJ9O/4iI2L6xbRPAehdiVYxzBQk/Lzjmo+Mfi619bsS99fcLbPY9B42hG/z86SpleY096TNPEHT2wTH5rVfCdZToeOXwfBG/jHYIqCgvfZah6xw6kH0Vf7MIXzD3KzrIUVgbBOf45NtqseZxZ/z6/+yWr2Ton6jmJcO31EmxPEKNhDLySb0x2COardWOCdJNlXz6i1/Nbh9Bx+mG3dMf36XrJXc0yoHH3/sPJFYVVJLnA8Kg0HS8RuP9oZ+Z3AXdDiG+Ao8yxuwlSFwklW9PYyt87BtjB0sCFc1RBXaCylAcXg+UOpFNa0v4L559Kbg4=j5S9nxmFJ+KFN/yiUMTlgw==; _uop_id=f644e6df867314b39a5717496fd542e9; loginflag=true; MII=000100030001; security_session_verify=9f2b0cd6a88f31de2b0ae9ac8a1d995b'


# 对cookie进行处理，处理成(key：value)格式
cookies = {i.split('=')[0]: i.split("=")[1] for i in cookie.split('; ')}



# 构造身份证验证请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36nameAccount: 4008588180uid: 8378356736cb: JSONP_CALLBACK_10_24',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Content-Length': '36',
    'Cookie': 'route=01d00cf1787a1004e23d35a9ed69aaab; SHOP_PROV_CITY=; _n3fa_cid=25fbf85f7dd9409592268c365ad40d49; _n3fa_ext=ft=1571287597; tianjincity=11|110; tianjin_ip=0; u_mobilePhone=; u_psptId=; USER_NAME=%E9%99%88%E9%9B%84%E5%B3%B0; mallchannel=06-0322-2383-9999; Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1571290568; UID=qGohrgz5Eh2k4MMzqJFQUXwZqRrFbTEU; MUT_V=null; backUrl=http://www.10010.com; loginType=06; Hm_lpvt_9208c8c641bfb0560ce7884c36938d9d=1571358556; _ga=GA1.2.1024364920.1571358557; _gid=GA1.2.56675778.1571358557; mall=Q1rc47c_Okb2aIgJDVM64LdlArXFkJJuyfdCHcWj3FcXWKNQ5rzc!-529603223; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571295112,1571302536,1571358605,1571368985; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571368985; piw=%7B%22login_name%22%3A%22176****1457%22%2C%22nickName%22%3A%22%E9%99%88%E9%9B%84%E5%B3%B0%22%2C%22rme%22%3A%7B%22ac%22%3A%22%22%2C%22at%22%3A%22%22%2C%22pt%22%3A%2201%22%2C%22u%22%3A%2217671451457%22%7D%2C%22verifyState%22%3A%22%22%7D; mallcity=71|710; citycode=710; userprocode=071; WT_FPC=id=27c47e18af7a95065891571287580211:lv=1571369092033:ss=1571368978087; mallflag=null; security_session_verify=17066a9f271b1872b7f92d4678b8bc33; JUT=k7I/hPnOUYgDTlhjKZ9IBdB/IgMZrWWdscQg+XtqjhXPVJ8Lq9N0MqEApKSfr6W258/llOeg2ljBOIpvpyoNcWAP4GTd8JsE1Io1U3zswYM4xF3IcZ7BsG7EKFEnoRi7u80V70xKQh2i4EKzsYWZW6lHCFqfEYszJahNpTB4tERKGXrJIS4t6NPO7O3Bqni27OALJRM+YmKsl0VlFIA6kkTMAv+xWvDVZqY8oHW2cruCJ9O/4iI2L6xbRPAehdiVYxzBQk/Lzjmo+Mfi619bsS99fcLbPY9B42hG/z86SpleY096TNPEHT2wTH5rVfCdZToeOXwfBG/jHYIqCgvfZah6xw6kH0Vf7MIXzD3KzrIUVgbBOf45NtqseZxZ/z6/+yWr2Ton6jmJcO31EmxPEKNhDLySb0x2COardWOCdJNlXz6i1/Nbh9Bx+mG3dMf36XrJXc0yoHH3/sPJFYVVJLnA8Kg0HS8RuP9oZ+Z3AXdDiG+Ao8yxuwlSFwklW9PYyt87BtjB0sCFc1RBXaCylAcXg+UOpFNa0v4L559Kbg4=j5S9nxmFJ+KFN/yiUMTlgw==; _uop_id=f644e6df867314b39a5717496fd542e9; loginflag=true; MII=000100030001',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Connection': 'keep-alive',
    'Host': 'iservice.10010.com',
    'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html?_=1571375904855',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': "https://iservice.10010.com",
}

# 身份验证接口地址
code_url = 'https://iservice.10010.com/e3/static/query/verificationSubmit_num?_=1571375973911&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html?_=1571375904855&'

# 构造身份验证请求体
code_data ={
    'menuid': '000100030001',
    'inputcode': '227915',
}

# 发送身份证验证请求
resp = requests.post(code_url,headers=headers,data=code_data)
# print(resp.status_code)
# print(resp.content.decode())

# 构造查询通讯记录请求体
datax={
    'pageNo': '1',
    'pageSize': '40',
    'beginDate': '20191001',
    'endDate':'20191017',
}
#
# 请求的url地址
url='https://iservice.10010.com/e3/static/query/callDetail?_=1571293178840&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html?_=1571290662589&menuid=000100030001'
#
# url = 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html'
#
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36nameAccount: 4008588180uid: 8378356736cb: JSONP_CALLBACK_10_24'
}
#
# url1 = 'https://iservice.10010.com/e3/static/query/sendRandomCode?_=1571360890487&'
#
# form_data = {
#     "accessURL": "https://iservice.10010.com/e4/query/bill/call_dan-iframe.html",
#     "menuid": "000100030001"
# }
#
# response = requests.post(url=url1, params=form_data,headers=headers,cookies=cookies)
#
# print(response.content.decode())
#
#

# 请求通讯记录json数据
response = requests.post(url=url,headers=headers,data=datax,cookies=cookies)

json_str = response.content.decode()
print(json_str)

# 将json字符串转换成字典
dict_str = json.loads(json_str)

# 处理成列表，形式  [{},{},{},{}]
result_list = dict_str['pageMap']['result']

print(result_list)
# 输出到Excel格式
export_excel(result_list)


