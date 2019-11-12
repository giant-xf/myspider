# coding=utf-8
'''
不需要图片验证码
短信登录
'''
import requests

def get_message_code(phone,session):
    url = 'https://fj.ac.10086.cn/SMSCodeSend?'
    params = {
        'spid': '40288367571d8d890157213f268f0001',
        'mobileNum': phone,
        'validCode': 'undefined',
        'errorurl': 'https://wap.fj.10086.cn/servicecb/common/errorPage.jsp',
        'name': 'menhu',
    }
    r = session.get(url, params=params)
    # print r.text
    if u"尊敬的用户，由于您操作频繁，暂时无法下发短信！！请过会再试！" in r.text:
        print u"尊敬的用户，由于您操作频繁，暂时无法下发短信！！请过会再试！"
    elif u"尊敬的客户，您好！您输入的手机号非福建移动号码，请您确认后再重试，谢谢！" in r.text:
        print u"尊敬的客户，您好！您输入的手机号非福建移动号码，请您确认后再重试，谢谢！"
    else:
        print u"尊敬的用户，短信验证码已发送到您的手机，请注意查收"



if __name__ == '__main__':
    session = requests.session()
    get_message_code('13799436651',session)
