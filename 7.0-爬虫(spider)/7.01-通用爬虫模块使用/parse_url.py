# coding=utf-8

import requests
from retrying import retry

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

# 尝试3次请求
@retry(stop_max_attempt_number=10)
def _parse_url(url, method, data, proxies):
    '''解析url'''
    print('*'*30)

    if method == 'POST':
        response = requests.post(url, headers=headers, data=data, proxies=proxies,verify=False)
    else:
        response = requests.get(url, headers=headers, timeout=3, proxies=proxies, verify=False)

    assert response.status_code == 200

    return response.content.decode()


def parse_url(url, method='GET',data=None, proxies={}):
    try:
        html_str = _parse_url(url, method, data, proxies)

    except:
        html_str = None

    return html_str


if __name__ == '__main__':
    url = 'https://www.baidu.com'
    print(parse_url(url))