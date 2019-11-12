# coding=utf-8
'''
不需要图片验证码
短信登录
'''

import os
import execjs
import requests
import random

base_url = 'https://wap.cq.10086.cn/wap'

# 加密
def encode_psswd(phone, pwd):
    base_dir = os.getcwd()
    js = execjs.compile(open(base_dir+"/js/chongqing_password.js").read().decode("utf-8"))
    ens = js.call('enstr',phone,pwd)
    return  ens #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数

# 获取短信验证码
def get_message_code(phone,session):
    params = {
        'service': 'ajaxDirect/1/touch.Login/touch.Login/javascript/',
        'pagename': 'touch.Login',
        'eventname': 'sendSmsPwd',
        'phoneNo': phone,
        'ID': 'undefined',
        'PAGERANDOMID': 'undefined',
        'ajaxSubmitType': 'get',
        'ajax_randomcode': '0.22791298403416538',
    }
    r =session.get(base_url, params=params)
    print r.text
    if u"随机密码已发送到您的手机，请使用登录！" in r.text:
        # return {'code':0}
        print u"随机密码已发送到您的手机，请使用登录！"

    elif u"您输入的号码非重庆移动号码。" in r.text:
        # return {'code':106}
        print u"您输入的号码非重庆移动号码。"

    elif u"您输入的号码非法。" in r.text:
        # return {'code':-1}
        print u"您输入的号码非法。"


def login(phone, session, sms_code):
    ens = encode_psswd(phone, sms_code)
    smsCheckPwd = ens.get('smsCheckPwd')
    pwd1 = ens.get('pwd1')
    params = {
        'service': 'ajaxDirect/1/touch.Login/touch.Login/javascript/',
        'pagename': 'touch.Login',
        'eventname': 'smsLogin',
        'phoneNo': phone,
        'smsCheckPwd': smsCheckPwd,
        'validateCode':'',
        'pwd_encoded': 'yes',
        'pwd1': pwd1,
        'ID': 'undefined',
        'PAGERANDOMID': 'undefined',
        'ajaxSubmitType': 'get',
        'ajax_randomcode': '0.29267880730249396',
    }
    r = session.get(base_url, params=params)
    print r.text
    if u"输入的短信密码或用户名错误，请重新获取！" in r.text:
        # return {'code':-1}
        print u"输入的短信密码或用户名错误，请重新获取！"


if __name__ == '__main__':

    session = requests.session()
    get_message_code('15823865453', session)
    sms_code =str(input('login sms code:'))
    login('15823865453',session,sms_code)
    print(encode_psswd('15823865453', '525113'))
