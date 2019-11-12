# coding=utf-8

'''
get_cookies()： 获得所有cookie信息。

get_cookie(name)： 返回字典的key为“name”的cookie信息。

add_cookie(cookie_dict) ： 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。

delete_cookie(name,optionsString)：删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。

delete_all_cookies()： 删除所有cookie信息。
'''

from selenium import webdriver
import time
import requests
from yundama.dama import indetify
option = webdriver.ChromeOptions()
option.binary_location=r'D:\谷歌浏览器\Google\Chrome\Application\chrome.exe'
#实例化driver
chrome_driver = r"D:\workon_home\spider_py3\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver,chrome_options=option)
driver.get("http://www.yundama.com/")

# driver.find_element_by_class_name("").click()

driver.find_element_by_id("username").send_keys("a819989150")
driver.find_element_by_id("password").send_keys("8023yue...")

# 识别验证码
captcha_image_url = driver.find_element_by_id("verifyImg").get_attribute("src")

# 获取本页的cookie信息
'''
IESESSION=alive; 
pgv_pvi=6703931392; 
pgv_si=s1348463616; 
_qddaz=QD.g39go9.ftokry.k1rupq3u; 
_qdda=3-1.1; 
_qddab=3-h1z49s.k1rupq3z; 
_qddamta_4008588180=3-0; 
tencentSig=2339917824; 
session=
'''
# cookie = driver.get_cookie('session')
# IESESSION = driver.get_cookie('IESESSION')
# pgv_pvi = driver.get_cookie('pgv_pvi')
# pgv_si = driver.get_cookie('pgv_si')
# _qddaz = driver.get_cookie('_qddaz')
# _qdda = driver.get_cookie('_qdda')
# _qddab = driver.get_cookie('_qddab')
# _qddamta_4008588180 = driver.get_cookie('_qddamta_4008588180')
# tencentSig = driver.get_cookie('tencentSig')
# session = driver.get_cookie('session')

# cookies = {
# 'IESESSION':IESESSION,
# 'pgv_pvi':pgv_pvi,
# 'pgv_si':pgv_si,
# '_qddaz':_qddaz,
# '_qdda':_qdda,
# '_qddab':_qddab,
# '_qddamta_4008588180':_qddamta_4008588180,
# 'tencentSig':tencentSig,
# 'session':session
# }

get_cookies = driver.get_cookies()      # 获取到的cookies
print(get_cookies)
cookies = {}                     # 你看到的cookie
# 拼接
for get_cookie in get_cookies:
    cookies[get_cookie['name']] = get_cookie['value']

print(cookies)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36nameAccount: 4008588180uid: 8378356736cb: JSONP_CALLBACK_10_24'
}

session = requests.session()
captcha_content = session.get(captcha_image_url,headers=headers, cookies=cookies).content
print(captcha_image_url)


captcha_code = indetify(captcha_content)
print("验证码的识别结果为:",captcha_code)

#输入验证码
driver.find_element_by_id("vcode").send_keys(captcha_code)

# time.sleep(5)
driver.find_element_by_class_name("sub").click()


# #获取cookie
# cookies = {i["name"]:i["value"] for i in driver.get_cookies()}
# print(cookies)

time.sleep(3)
driver.quit()