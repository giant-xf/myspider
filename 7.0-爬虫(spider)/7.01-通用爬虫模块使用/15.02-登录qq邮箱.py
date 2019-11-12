# coding=utf-8
from selenium import webdriver
import time
import requests
from yundama.dama import indetify
option = webdriver.ChromeOptions()
option.binary_location=r'D:\谷歌浏览器\Google\Chrome\Application\chrome.exe'
#实例化driver
chrome_driver = r"D:\workon_home\spider_py3\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver,chrome_options=option)
driver.get("https://mail.qq.com/cgi-bin/loginpage")

# 切换到iframe中
driver.switch_to.frame('login_frame')

driver.find_element_by_id("switcher_plogin").click()

driver.find_element_by_id("u").send_keys("819989150")
driver.find_element_by_id("p").send_keys("123456.+-")

# #识别验证码
# captcha_image_url = driver.find_element_by_id("captcha_image").get_attribute("src")
# captcha_content = requests.get(captcha_image_url).content
# captcha_code = indetify(captcha_content)
# print("验证码的识别结果为:",captcha_code)

# #输入验证码
# driver.find_element_by_id("captcha_field").send_keys(captcha_code)

time.sleep(5)
driver.find_element_by_id("login_button").click()


#获取cookie
cookies = {i["name"]:i["value"] for i in driver.get_cookies()}
print(cookies)

time.sleep(3)
driver.quit()