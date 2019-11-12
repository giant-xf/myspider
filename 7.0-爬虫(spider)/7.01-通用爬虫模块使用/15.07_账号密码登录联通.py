# coding=utf-8
import requests
import json
import time
import random
from selenium import webdriver
import xlwt
import pandas as pd
import re
import time
import logging
import calendar

class LiantongData(object):

    def __init__(self,mobile,pwd):
        self.session = requests.session()
        # 构造登录请求
        self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36nameAccount: 4008588180uid: 8378356736cb: JSONP_CALLBACK_10_24',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': 'SHOP_PROV_CITY=; _n3fa_cid=25fbf85f7dd9409592268c365ad40d49; _n3fa_ext=ft=1571287597; ckuuid=e0ece1f7487d35ab82e3af1f14f599e1; tianjincity=11|110; tianjin_ip=0; u_mobilePhone=; u_psptId=; MUT=a2e40328-468f-4fe5-8355-3ad1c14074c2; USER_NAME=%E9%99%88%E9%9B%84%E5%B3%B0; mallchannel=06-0322-2383-9999; Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1571290568; UID=qGohrgz5Eh2k4MMzqJFQUXwZqRrFbTEU; MUT_V=null; backUrl=http://www.10010.com; loginType=06; uacverifykey=hxz3c064daf4561046716b35e4f4f565d45akp; Hm_lpvt_9208c8c641bfb0560ce7884c36938d9d=1571358556; _ga=GA1.2.1024364920.1571358557; _gid=GA1.2.56675778.1571358557; mallcity=71|710; citycode=710; userprocode=071; WT_FPC=id=27c47e18af7a95065891571287580211:lv=1571368978098:ss=1571368978087; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571295112,1571302536,1571358605,1571368985; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571368985; unisecid=D0F801A53BEA5E4FA8C7069D87CF8F12',
    'Connection': 'keep-alive',
    'Host': 'uac.10010.com',
    'Referer': 'https://uac.10010.com/portal/homeLoginNew',
    'X-Requested-With': 'XMLHttpRequest',
}

        # 手机号和服务密码
        self.mobile = mobile
        self.pwd = pwd

        # 登录的url
        self.login_url = 'https://uac.10010.com/portal/Service/MallLogin'
        # 发送短信验证码
        self.get_message_code_url = 'https://uac.10010.com/portal/Service/SendCkMSG?callback=jQuery17205594122191004673_1571802024337&req_time=1571802046880&mobile={}&_=1571802046880'.format(self.mobile)
        # 获取图形验证码
        self.get_image_code_url = 'https://uac.10010.com/portal/Service/CreateImage?t=1571802039968'
        # 检查是否登录的url
        self.check_login_url = 'https://iservice.10010.com/e3/static/check/checklogin?_=1571485687726'
        # 二重检查登录状态的url
        self.checkmapExtraParam_url = 'https://iservice.10010.com/e3/static/query/checkmapExtraParam?_=1571485688788'
        # 发送短信验证码的url
        self.send_url = 'https://iservice.10010.com/e3/static/query/sendRandomCode?_=1571486814644&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html&menuid=000100030001'
        # 检查验证码正确性的url
        self.check_verification_url = 'https://iservice.10010.com/e3/static/query/verificationSubmit?_=1571484345965&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html&menuid=000100030001'
        # 查询数据
        self.data_url = 'https://iservice.10010.com/e3/static/query/callDetail?_=1571484346100&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html&menuid=000100030001'

        self.menuId = {'menuId': '000100030001'}

    def need_code(self):
        url = "https://uac.10010.com/portal/Service/CheckNeedVerify"
        params = {'callback': 'jQuery17205594122191004673_1571802024336', 'userName': self.mobile, 'pwdType': '01', '_': '1571802039865'}
        self.session.get(url,params=params)
        self.get_message_code()

    def get_message_code(self):
        resp = self.session.get(self.get_message_code_url)
        print(u"验证码发送成功")

    def login(self,verifyCKCode):
        '''
        账号密码登录
        :param username: 手机号
        :param pwd: 服务密码
        :return:
        '''
        # 登录的请求体构造
        login_data = {
            'callback': 'jQuery17206160369098513445_1571358605494',
            'req_time': '1571358627742',
            'redirectURL': 'http://www.10010.com',
            'userName': self.mobile,
            'password': self.pwd,
            'pwdType': '01',
            'productType': '01',
            'redirectType': '01',
            'rememberMe': '1',
            'verifyCKCode': verifyCKCode,
            '_': '1571358627743',
        }

        resp = self.session.get(self.login_url, headers=self.headers, params=login_data)
        print('登录是否成功状态码:'.format(resp.status_code))
        # print('重定向页面'.format(resp.content.decode()))

        # 查看登录后的cookie
        # cookies = requests.utils.dict_from_cookiejar(resp.cookies)
        # print(cookies)
        if resp.content.decode() is not None:
            print(resp.content.decode())
            code = re.findall(r'resultCode:"(.*?)"',resp.content.decode())[0]
            if code != '0000':
                print('服务密码有误')
                return 0
            return 1
        else:
            print('请求报错')

    # def get_image_code(self):
    #     self.session.get(self.get_image_code_url)

    def check_login(self):
        '''
        检查登录状态
        :return:
        '''
        # 检查登录状态的url
        resp = self.session.post(self.check_login_url)
        print(u'检查登录状态:{}'.format(resp.status_code))
        print(resp.text)

    def check_login_result(self):
        '''
        检查是否登录的结果
        :return:
        '''
        resp = self.session.post(self.checkmapExtraParam_url, data=self.menuId)
        print(u'检查是否检查登录状态:{}'.format(resp.status_code))
        print(resp.content.decode())

    def send_random_code(self):
        '''
        发送短信验证码
        :return:
        '''
        resp = self.session.post(self.send_url, data=self.menuId)
        print('u发送短信状态:{}'.format(resp.status_code))
        print(resp.content.decode())
        sendcode = json.loads(resp.content.decode())["sendcode"]
        # print(sendcode)
        if sendcode != True:
            print('短信验证码发送失败')
            return 0
        return 1

    def check_verification(self,verify):
        # 构造验证码请求体
        check_verification_data = {
            'inputcode': verify,
            'menuId': self.menuId
        }

        resp = self.session.post(self.check_verification_url, data=check_verification_data)
        print(u'验证短信验证码是否正确:{}'.format(resp.status_code))
        print(resp.content.decode())
        if json.loads(resp.content.decode())['flag'] !='00':
            print(u'验证码输入错误或者查询次数过多，请稍后查询！')
            return 0
        return 1

    def check_idcard_code(self,idcard):
        url = 'https://iservice.10010.com/e3/static/query/verificationSubmit_num?_=1571484346100&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html&menuid=000100030001'
        data = {
            'inputcode': idcard,
            'menuId': '000100030001'
        }
        self.session.post(url, data, headers={'X-Requested-With': 'XMLHttpRequest'})
        print(u'身份证验证发送')

    def query_data(self,start_time,end_time):
        '''
        查询通讯记录
        :return:
        '''
        # 构造查询通讯记录请求体
        data_data = {
            'pageNo': '1',
            'pageSize': '20',
            'beginDate': start_time,
            'endDate': end_time
        }

        resp = self.session.post(self.data_url, data=data_data)
        json_str = resp.text

        # 输出json字符串
        print(json_str)

        try :
            # 将json字符串转换成字典
            dict_str = json.loads(json_str)

            # 处理成列表，形式  [{},{},{},{}]
            result_list = dict_str['pageMap']['result']
            print(result_list)
        except Exception as e:
            logging.warning(e)

        # # 输出到Excel格式
        # self.export_excel(result_list)

        return result_list

    def get_balance(self):
        url = 'https://iservice.10010.com/e3/static/realtimewo/accountbalancewo?_=1572252576347'
        data = {
            'chargetype': 0
        }

        resp = self.session.post(url=url, data=data)
        resp = json.loads(resp.text)
        print '剩余余额为: {}元'.format(resp['result']['balance'])


    def get_year_month(self, n):
        '''获取n个月前的年份和月份和天数'''
        day_now = time.localtime()
        year0 = day_now.tm_year
        month0 = day_now.tm_mon

        print(day_now, year0, month0)

        monthx = month0 - n
        yearx = year0
        if monthx < 1:
            yearx = year0 - n
            monthx = month0 + 12 - n

        day_begin = '%d%02d01' % (yearx, monthx)  # 月初肯定是1号
        wday, monthRange = calendar.monthrange(yearx, monthx)  # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
        day_end = '%d%02d%02d' % (yearx, monthx, monthRange)

        day_begin2 = '%d-%02d-01' % (yearx, monthx)
        day_end2 = '%d-%02d-%02d' % (yearx, monthx, monthRange)

        return yearx, monthx, day_begin, day_end, monthRange, day_begin2, day_end2

    def export_excel(self,data):
        '''
        保存到Excel格式
        :param data: 传入字典列表
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


    def pwd_login_run(self):
        pass

    def verify_login_run(self):
        pass


if __name__ == '__main__':

    mobile = input('请输入联通手机号:')
    pwd = input('请输入6位数服务密码:')

    liantong = LiantongData(mobile, pwd)
    verifyCKCode = liantong.need_code()
    verifyCKCode = input('请输入验证码:')
    if liantong.login(verifyCKCode) == 0:
        print(u'登录失败')
    print(u'登录成功!')

    liantong.check_login()
    idcard = input('请输入身份证后6位')
    liantong.check_idcard_code(idcard)

    print '=' * 50
    liantong.get_balance()
    print '=' * 50

    n = int(input('请输入要查询本月前几个月(n>=0):'))
    time = liantong.get_year_month(n)
    start_time, end_time = time[2], time[3]
    #
    print(u'您要查询的时间:{}至{}'.format(start_time, end_time))
    data = liantong.query_data(start_time,end_time)
    liantong.export_excel(data)
    print(u'执行完毕，数据存成功')

    # time.sleep(10)
    # liantong.check_login()
    # liantong.check_login_result()
    # if liantong.send_random_code() !=0:
    #     # 检查联通验证码
    #     verify = input('请输入短信验证码:')
    #     if liantong.check_verification(verify) !=0:
    #         n = int(input('请输入要查询本月前几个月(n>=0):'))
    #         time = liantong.get_year_month(n)
    #         start_time, end_time = time[2], time[3]
    #         #
    #         print('您要查询的时间:{}至{}'.format(start_time, end_time))
    #         data = liantong.query_data(start_time,end_time)
    #         liantong.export_excel(data)
    #         print('执行完毕，数据存成功')


#https://iservice.10010.com/e3/static/query/sendRandomCode?
# _=1571484294549
# &accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html
# &menuid=000100030001


# resp = session.get('https://iservice.10010.com/e4/query/bill/call_dan-iframe.html')
# print('查询通话记录页面跳转:{}'.format(resp.status_code))
# print(resp.content.decode())


# 检查登录状态
# https://iservice.10010.com/e3/static/check/checklogin?_=1571485687726




# 查询检查结果
# https://iservice.10010.com/e3/static/query/checkmapExtraParam?_=1571485688788


# 发送短信请求头构造
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36nameAccount: 4008588180uid: 8378356736cb: JSONP_CALLBACK_10_24',
#     'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'Cookie': 'SHOP_PROV_CITY=; _n3fa_cid=25fbf85f7dd9409592268c365ad40d49; _n3fa_ext=ft=1571287597; ckuuid=e0ece1f7487d35ab82e3af1f14f599e1; tianjincity=11|110; tianjin_ip=0; u_mobilePhone=; u_psptId=; MUT=a2e40328-468f-4fe5-8355-3ad1c14074c2; USER_NAME=%E9%99%88%E9%9B%84%E5%B3%B0; mallchannel=06-0322-2383-9999; Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1571290568; UID=qGohrgz5Eh2k4MMzqJFQUXwZqRrFbTEU; MUT_V=null; backUrl=http://www.10010.com; loginType=06; uacverifykey=hxz3c064daf4561046716b35e4f4f565d45akp; Hm_lpvt_9208c8c641bfb0560ce7884c36938d9d=1571358556; _ga=GA1.2.1024364920.1571358557; _gid=GA1.2.56675778.1571358557; mallcity=71|710; citycode=710; userprocode=071; WT_FPC=id=27c47e18af7a95065891571287580211:lv=1571368978098:ss=1571368978087; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571295112,1571302536,1571358605,1571368985; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571368985; unisecid=D0F801A53BEA5E4FA8C7069D87CF8F12',
#     'Connection': 'keep-alive',
#     'Host': 'uac.10010.com',
#     'Referer': 'https://uac.10010.com/portal/homeLoginNew',
#     'X-Requested-With': 'XMLHttpRequest',
#
# }
# https://iservice.10010.com/e3/static/query/sendRandomCode?_=1571484294549&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html&menuid=000100030001







# 验证码检验
# https://iservice.10010.com/e3/static/query/verificationSubmit?_=1571484345965&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html&menuid=000100030001
