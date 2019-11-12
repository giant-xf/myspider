# coding=utf-8
import requests
import re
import time
import calendar as cal
def get_month_list(ft='normal', start_date=None):
    now = time.localtime()
    month_count = 6
    if start_date:
        month_diff = (now.tm_year - start_date.year) * 12 + now.tm_mon - start_date.month + 1
        month_count = month_diff if month_diff < 6 else 6
    month_list = [time.localtime(time.mktime((now.tm_year, now.tm_mon - n, 1, 0, 0, 0, 0, 0, 0)))[:2] for n in range(month_count)]
    if ft == 'normal':
        return ['%d%02d' % (y, m) for y, m in month_list]
    elif ft == 'Y-M-01':
        return ['%d-%02d-01' % (y, m) for y, m in month_list]
    elif ft == 'Y-M':
        return ['%d-%02d' % (y, m) for y, m in month_list]
    elif ft == 'tuple':
        return month_list
    elif ft == 'fromto':
        fromto_monthlist = []
        for index, ym in enumerate(month_list):
            if index == 0:
                fromto_monthlist.append(['%d-%02d-01' % (ym[0], ym[1]), '%d-%02d-%02d' % (ym[0], ym[1], now.tm_mday)])
            else:
                d = cal.monthrange(ym[0], ym[1])
                fromto_monthlist.append(['%d-%02d-01' % (ym[0], ym[1]), '%d-%02d-%02d' % (ym[0], ym[1], d[1])])
        return fromto_monthlist



session = requests.session()
dict = {}
url = 'http://wap.js.10086.cn/WDZL.thtml'
headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'XWBD_SESSIONID=S110517484052903156; mywaytoopen=e1c90e81345246acdb566f02ba392c86; userMobileForBigData=13775385744; userAreaNum=18; Hm_lvt_416c770ac83a9d996d7b3793f8c4994d=1573007123; Hm_lpvt_416c770ac83a9d996d7b3793f8c4994d=1573007538; DZQDPAACTK=bb427514db2a2c1aee46b214c3f26a61; cmtokenid=2D027CBA40E346639EC4FE1408EF16C3@js.ac.10086.cn; CmWebtokenid=13775385744,js; autoLogin=2CBD81EFF6FE46C427AD5F8EA9B0296018971D862B8AFD8D; last_success_login_mobile=13775385744; 13775385744_XJYH_XESJYQB=4f8b94e8; 13775385744_XJYH_AQYHY=918781cb; 13775385744_null=fde8e979; 13775385744_XJYH_QQLYTHY=632d3c39; 13775385744_12580HSH10Y=3d1301ae; 13775385744_XJYH_XMCBHY=6b6baa58; 13775385744_XJYH_BESTVHY=28c59f54; 13775385744_XJYH_RWGCHY=ee7604b2; 13775385744_XJYH_CZLYHY=a798f559; 13775385744_XJYH_YHASEHY=b759f363; tid=2jm1afuk2mobasr; nid=1kaok2moe5uf; JSESSIONID=rx0-m_3jEzPFn2fOl474id8Z2YkiaQi0dON9Dq1Mt5RZPAdY8tNc!100111769; WT_FPC=id=24c73796d1a687d436d1573007122714:lv=1573008585452:ss=1573007122714',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',

}

r = session.get(url, headers=headers)
in_net_date = re.compile('(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})').findall(r.text)[0]
dict['in_net_date'] = in_net_date
print in_net_date

url = 'http://wap.js.10086.cn/ZHYEJYXQ.thtml'
r = session.get(url, verify=False)
data = r.text.replace('<\\', '<')
cost = re.compile(u'话费账户余额<\/td><td>(.+?)<').findall(data)[0]
dict['cost'] = cost
print cost


browserUA = 'Mozilla/5.0 {Windows NT 6.1; WOW64} AppleWebKit/537.36 {KHTML, like Gecko} Chrome/75.0.3770.100 Safari/537.36'
months = get_month_list()
name_flag = 1
for month in months:
    url = 'http://wap.js.10086.cn/actionDispatcher.do'
    data = {
        'reqUrl': 'ZDCXGB',
        'ver': 't',
        'busiNum': 'ZDCX',
        'beginDate': month,
        'phone': '13775385744',
        'isFamily': '1',
        'browserUA': browserUA,
    }
    r = session.post(url, data=data, verify=False)
    bill = float(r.json()['resultObj']['billBean']['billRet']['totalFee']) / 100.0
    print '{}月的消费为:{}'.format(month,bill)
    name = r.json()['resultObj']['billBean']['userInfoBean']['userName']
    if dict and name_flag:
        dict['name'] = name
        name_flag = 0

print dict


'''
resultObj":{"months":["201906","201907","201908","201909","201910","201911"],"ch":"","wjdc":{},"line":"'12月' : 225.69,'1月' : 186.79,'2月' : 157.74,'3月' : 169.14,'4月' : 167.42,'5月' : 168.10,'6月' : 182.71,'7月' : 174.10,'8月' : 154.20,'9月' : 189.90,'10月' : 228.63,'11月' : 30.90"
'''

'''
"resultObj":{"months":["201906","201907","201908","201909","201910","201911"],"ch":"","wjdc":{},"line":"'12月' : 225.69,'1月' : 186.79,'2月' : 157.74,'3月' : 169.14,'4月' : 167.42,'5月' : 168.10,'6月' : 182.71,'7月' : 174.10,'8月' : 154.20,'9月' : 189.90,'10月' : 228.63,'11月' : 30.90",
'''