# coding=utf-8

from selenium import webdriver
import time
import requests
import json
import xlwt
import pandas as pd

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

def get_year_month(n):
    '''获取n个月前的年份和月份和天数'''
    day_now = time.localtime()
    year0 = day_now.tm_year
    month0 = day_now.tm_mon

    print(day_now,year0,month0)

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



option = webdriver.ChromeOptions()
option.binary_location=r'D:\谷歌浏览器\Google\Chrome\Application\chrome.exe'
#实例化driver
chrome_driver = r"D:\workon_home\spider_py3\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver,chrome_options=option)

# driver.get('https://uac.10010.com/portal/mallLogin.jsp')
driver.get('https://iservice.10010.com/e4/query/bill/call_dan-iframe.html?_=1571290662589')

# 切换到iframe中
driver.switch_to.frame(1)

time.sleep(5)

driver.find_element_by_class_name("randomCodeLogin").click()

driver.find_element_by_id('userName').send_keys("17671451457")

time.sleep(1)
# 点击获取验证码
driver.find_element_by_id("randomCode").click()


time.sleep(15)
driver.find_element_by_id("login1").click()

time.sleep(5)

# 填入身份信息
driver.find_element_by_id('input_num').send_keys('227915')
driver.find_element_by_id('sign_in_num').click()

#获取cookie
cookies = {i["name"]:i["value"] for i in driver.get_cookies()}
print(cookies)

# 构造请求数据
datax={
    'pageNo': '1',
    'pageSize': '40',
    'beginDate': '20191001',
    'endDate':'20191017',
}
url='https://iservice.10010.com/e3/static/query/callDetail?_=1571293178840&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html?_=1571290662589&menuid=000100030001'

# todo:由于短信上限制了。我自己登入之后提取了cookie测试后面功能
# cookie ='JSESSIONID=946B39AE44B71D4C2402D93007099BD5; route=f6580975dacd2642305771459ba78210; e3route=c46ea420375f2b0dfa96a05e2c3e9a55281e236f; SHOP_PROV_CITY=; _n3fa_cid=25fbf85f7dd9409592268c365ad40d49; _n3fa_ext=ft=1571287597; tianjincity=11|110; tianjin_ip=0; u_mobilePhone=; u_psptId=; MUT=a2e40328-468f-4fe5-8355-3ad1c14074c2; USER_NAME=%E9%99%88%E9%9B%84%E5%B3%B0; mallchannel=06-0322-2383-9999; Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1571290568; Hm_lpvt_9208c8c641bfb0560ce7884c36938d9d=1571290568; UID=qGohrgz5Eh2k4MMzqJFQUXwZqRrFbTEU; MUT_V=null; backUrl=http://www.10010.com; loginType=06; WT_FPC=id=27c47e18af7a95065891571287580211:lv=1571295088862:ss=1571295088847; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571287597,1571290369,1571295112; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1571295112; piw=%7B%22login_name%22%3A%22176****1457%22%2C%22nickName%22%3A%22%E9%99%88%E9%9B%84%E5%B3%B0%22%2C%22rme%22%3A%7B%22ac%22%3A%22%22%2C%22at%22%3A%22%22%2C%22pt%22%3A%2201%22%2C%22u%22%3A%2217671451457%22%7D%2C%22verifyState%22%3A%22%22%7D; _uop_id=56f7e1bcf1bbba64bdbca80807edeecd; userprocode=071; citycode=710; mallcity=71|710; loginflag=true; mallflag=null; JUT=LC95vyFOGdxY/7RKjR/eS+Gk6aT0puvNauTNcDTwwMDhpGTAtoavlZ6wu7XQHA9Nkh/xVEFz+vXrBhijJBhLUsgOmC9URptV0o7tQs9Ke1BJMO3v83uIKd6cePiXnSK3IFoef0bQ9v1wVxTeBS8TsvTmqhpEtPOkDsqZwt1c/4MCu3yxSBnaZNDzdYssBwAECwOhGI+aENk5Jg1HjEcIEwPnvkX2M3u7OLuNlHjqIVjJGlCxUM8JA2ZeahV9J9VVNobP8v1wyfOmTGrME3Slqc/Lg2JP9lZCwJMoSJ6/OtgUUJHxv9Thc5IHPcbN5HQbdtKeB9/PHUzTZAclG5//7fJmbcMsrZu7SFTeBZJf7E4UgCjVnudOKzJuc0tkZwETdaWT6MI3inL8w8hsO0dtmHJULLMD8+jEug5XObQszxIsMPXs3XAGASbKNhoIkEcAY+Hsqus3lTMzFyiyksEYJsywPzVyAe5uT9ZjvBxcBQTLWaQgsz9AZajygFwpoCBzAeqJf1azC2Q8bRQgWbrpLfU/vag+r87kGZBBzSa40rrsdRa5Tr8CdA==; security_session_verify=310d2e5359703501b1c39a7cc462ae46; MII=000100030001'
#
# cookies = {i.split('=')[0]: i.split("=")[1] for i in cookie.split('; ')}

# 构造数据
datax={
    'pageNo': '1',
    'pageSize': '40',
    'beginDate': '20191001',
    'endDate':'20191017',
}

# 请求的url地址
url='https://iservice.10010.com/e3/static/query/callDetail?_=1571293178840&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html?_=1571290662589&menuid=000100030001'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36nameAccount: 4008588180uid: 8378356736cb: JSONP_CALLBACK_10_24'
}

response = requests.post(url=url,headers=headers,data=datax,cookies=cookies)

dict_str = json.loads(response.content.decode())

result_list = dict_str['pageMap']['result']

print(result_list)
# 输出到Excel格式
export_excel(result_list)

# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
# }
#
# response = requests.get('https://iservice.10010.com/e4/query/bill/call_dan-iframe.html?_=1571290662589', headers=headers, cookies=cookies)
#
# with open('联通.txt', 'w', encoding='utf-8') as f:
#     f.write(response.content.decode())

# print(response.content.decode())

time.sleep(2)
driver.quit()
