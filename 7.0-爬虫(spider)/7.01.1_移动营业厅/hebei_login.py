# coding=utf-8
'''
需要图片验证码
服务密码登录
'''
import requests
import random
import uuid
import os
from lxml import html
import time

def get_image_code(phone, session):
    url = 'http://he.ac.10086.cn/common/image.jsp?r={}'.format(random.random())
    r = session.get(url)
    # 拼接出目录
    file_dir = os.path.join(os.getcwd(), 'images', 'hebei', time.strftime("%Y%m%d", time.localtime()))
    # 创建目录
    os.makedirs(file_dir)
    # 拼接出图片路径
    image_path = os.path.join(file_dir,'img{}.{}'.format(uuid.uuid3(uuid.NAMESPACE_DNS,'python.org'),'jpg'))
    print image_path
    with open(image_path,'wb') as f:
        f.write(r.content)

def get_message_code(phone,session,img_code):
    url = 'https://fj.ac.10086.cn/SMSCodeSend?'
    params = {
        'mobileNum': phone,
        'validCode': img_code,
        'spid': '8af849a35584353601566830336c0001',
        'warnurl': 'http://wap.he.10086.cn/touch/warnPage.jsp',
    }
    r = session.get(url, params=params)
    print r.text

def gen_dict(text, prefix=''):
    root = html.fromstring(text)
    return dict(
        [(''.join(input.xpath('@name')),
          ''.join(input.xpath('@value'))) for input in root.xpath('{}//input'.format(prefix)) if input.xpath('@name') and input.xpath('@value')
         ])


if __name__ == '__main__':
    session = requests.session()
    # url = 'http://wap.he.10086.cn/touch/login.action?continueUrl=http://wap.he.10086.cn/touch/my.action?menuid=mine'
    # r = session.get(url)
    # # print r.text
    # data = gen_dict(r.text)
    # print data
    #
    # url = 'http://he.ac.10086.cn/POST'
    # r = session.post(url, data=data)
    # # print r.text
    # data = gen_dict(r.text)
    # print data
    # url = 'http://wap.he.10086.cn/touch/login!initLogin.action'
    # r = session.post(url,data=data)
    # data = gen_dict(r.text,prefix='//form[@name="loginForm"]')
    # print data
    # url = 'https://he.ac.10086.cn/Login'
    # data.update({
    #     'mobileNum': '13400105561',
    #     'servicePassword': 'ED0BE947859F065E762275E71F85EEFB',
    #     'validCode': 't6me',
    #     'validCode1': 't6me',
    #     'smsValidCode': '',
    # })
    # r = session.post(url, data=data)
    # print r.url


    # {'backurl': 'http://wap.he.10086.cn/touch/login!initLogin.action',
    #  'RelayState': 'spid=8af849a35584353601566830336c0001;type=B;backurl=http%3A%2F%2Fwap.he.10086.cn%2Ftouch%2Flogin%21initLogin.action;nl=1;continue_url=http%3A%2F%2Fwap.he.10086.cn%2Ftouch%2Fmy.action%3Fmenuid%3Dmine%26from%3DH5;loginType=2;authlevel=B',
    #  'loginType': '2',
    #  'warnurl': 'http://wap.he.10086.cn/touch/warnPage.jsp',
    #  'spid': '8af849a35584353601566830336c0001',
    #  'type': 'B'
    #  }


    get_image_code('13400105566',session)
    img_code = input('login image code:')
    get_message_code('13799436651',session,img_code)
