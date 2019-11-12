

import requests


# url_temp = 'https://www.baidu.com/s?'
# p = {'wd':'传智播客'}
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
# response = requests.get(url_temp, headers=headers, params=p)

'''
# 这里字符串拼接可以用%s，也可以用
url = 'https://www.baidu.com/s?wd={}'.format('传智播客')
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

# 自定义请求头，模拟浏览器的标识
response = requests.get(url, headers=headers)

with open('传智播客.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
    print('保存成功')

print(response.status_code)
print(response.request.url)
'''


# img_url = "http://www.hue.edu.cn/static/image/logo.gif"
img_url = "http://www.hue.edu.cn/upload/2019-07-07/229e47d3-096d-4995-93fe-a7e95af62597.png"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

response = requests.get(img_url, headers= headers)

with open("logn.png", "wb") as f:
    f.write(response.content)
    print('保存成功')



