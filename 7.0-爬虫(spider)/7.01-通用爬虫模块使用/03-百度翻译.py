# coding=utf-8

import requests
import json
from lxml import etree
import re
import execjs
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# fanyi_url = 'http://m.youdao.com/translate'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
#
# data = {
#     'inputtext': '人生苦短，我用python',
#     'type': 'AUTO'
# }

# fanyi_url = 'https://fanyi.baidu.com/basetrans'
#
# headers = {
#      'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
#
# data = {
# 'query': '人生苦短，我用python',
# 'from': 'zh',
# 'to': 'en',
# # 'token': '628dee0dff2c3f7af0a98950890da13b',
# # 'sign': '289133.35420'
# }
#
# r = requests.post(fanyi_url, headers=headers, data=data)
#
# print(r.content.decode())

class BaiduFanyi(object):
     '''翻译类'''
     def __init__(self, trans):
          self.lang_detect_url = 'https://fanyi.baidu.com/langdetect'
          self.trans = trans
          self.url = 'https://fanyi.baidu.com/basetrans'
          self.token_sign_url = 'https://fanyi.baidu.com/?aldtype=16047'
          self.headers ={
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

     def parse_url(self,session,  url, data):
          '''发送post请求'''
          response = session.post(url, data=data, headers=self.headers)
          # 将json字符串转换成字典
          return json.loads(response.content.decode())


     def get_ret(self, dict_response):
          '''获取翻译结果'''
          # 这里接收不到正确的200响应数据
          # print(dict_response)
          ret = dict_response["trans"][0]['dst']
          print('翻译结果为:',ret)

     def run(self):
          session = requests.session()
          session.get(self.token_sign_url).text
          html = session.get(self.token_sign_url).text
          # print (html)
          token = re.findall(r"token: '(.*?)',", html)[0]
          # print(token)
          # 1.获取翻译的语言类型('zh','en')
               # 1.1 准备post的url地址
          lang_detect_data = {'query': self.trans}
               # 1.2 发送post请求，获取响应
               # 1.3 提取语言类型
          lang = self.parse_url(session,self.lang_detect_url, lang_detect_data)['lan']
          print ('语言类型为:{}'.format(lang))
          with open('baidujs.js') as f:
               jsData = f.read()
          # print(jsData)
          sign = execjs.compile(jsData).call("e", self.trans)

          # 2.准备post的数据
          trans_data = {'query': self.trans,'from': 'zh','to':'en','token': token,'sign': sign} if lang=='zh' else {'query': self.trans,'from': 'en','to':'zh','token': token,'sign': sign}
          # print(trans_data)
          # 3.发送请求，获取响应
          dict_response = self.parse_url(session,self.url, trans_data)
          # 4.提取翻译结果
          self.get_ret(dict_response)


if __name__ == '__main__':
     trans = ''
     while trans!='q':
          trans = input('请输入需要翻译的类容(退出请输入q):')
          if trans == 'q':
               break
          baidu_fanyi = BaiduFanyi(trans)
          baidu_fanyi.run()









'''
BIDUPSID=793B7FBE2161DAE52CA942F7B949C948; BAIDUID=54F20F08A95F4B9EF5726599DF9AA41E:FG=1; PSTM=1565963658; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_0_0=1; H_WISE_SIDS=134725_126886_132921_100806_134877_135070_126064_120125_134721_132757_132910_131247_130763_132378_131517_118894_118870_118854_118826_118805_107319_132783_122035_133351_132553_129652_132250_134855_128967_135307_133838_133847_132552_135432_135874_134256_131423_135473_135858_136018_135632_110085_134153_127969_131753_131953_135623_135461_127416_135046_135042_134096_135834_134383_133667_135504_134352_100460; __cfduid=dfbd720810e0281f27e8627e899e26b4f1568885509; BDUSS=JpM3hQc0IyUlpmQmR-dnNpTU5nV3dhVkdwZ1VMU2pyVHZzQUtYZGxkRjVhclJkRVFBQUFBJCQAAAAAAAAAAAEAAABgE8HDejFqSGJMNzlwdDEzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHndjF153YxdTE; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1990_1446_21112_29568_29221; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1570699300,1570774097,1570947525,1571035072; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1571044644; delPer=0; locale=zh; ZD_ENTRY=baidu; PSINO=3; pgv_pvi=6125440000; pgv_si=s3697061888; to_lang_often=%5B%7B%22value%22%3A%22spa%22%2C%22text%22%3A%22%u897F%u73ED%u7259%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22pt%22%2C%22text%22%3A%22%u8461%u8404%u7259%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1571156011; yjs_js_security_passport=06b643c30b95b678fa245b8c5000b8387c8fde28_1571157130_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1571157132; __yjsv5_shitong=1.0_7_db6c67e31d3c2e584380c4e5e242f6c8664d_300_1571157132205_183.95.249.228_4398306b
'''

