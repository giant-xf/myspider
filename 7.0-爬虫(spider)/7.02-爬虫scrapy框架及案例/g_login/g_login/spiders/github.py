# -*- coding: utf-8 -*-
import scrapy
import re

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    # cookies ="_octo=GH1.1.107814229.1566227509; _ga=GA1.2.2130801892.1566227638; _device_id=c4c0579d69bb8fc5beaea1ec59b2bd82; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai; user_session=oGWi6x3iIDByWaG0clI1iyOEKsG2xVjT8_usXVQ6fTxOq6zx; __Host-user_session_same_site=oGWi6x3iIDByWaG0clI1iyOEKsG2xVjT8_usXVQ6fTxOq6zx; logged_in=yes; dotcom_user=giant-xf; _gh_sess=ajFwR0ovWVk3M3dBV1Z0NENJc29WWWtsRUJaY1JjVGdiY0w4a2FPeFRnaVd5WEJLUUIxZlh6SDBwWnNtVUs1aWNRWC9CK0hYY01jd3hjYVJTR0NveXdLSU5QQ0MzN0lQam9iZFpaMndBcE03cU94azh2dG5hRGk5enB5a1V1eW85ekNIZURvRkpwUTVXYXkvSDh6TW5HV3gvZVVSUTQzUzY5c1ZzZ200dVBWQ3V2WHRwVUM2MlppUEtlT29IcDRuZndnQ2ZoNW4zakJhZEg4NmpIWnRPZz09LS1uN3FNZFNDYmJDM1AxVjdxUHJ4NnpBPT0%3D--b605add7d548833f3679d7a70c1bb8e122d2bdce"
        # cookies = { i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
        # yield scrapy.FormRequest(
        #     url= 'https://github.com/session',
        #     callback=
        # )

    def parse(self, response):
        # commit: Sign in
        # utf8: ✓
        # authenticity_token: a + aUKA5f + szBMX23ZV4Uz4xMPn1c4b76lk + t0z + rN9kNnsriOxI26T9nMeHI4btkwOGba + OP9c6hMNs / 5U0KVg ==
        # login: giant - xf
        # password: 819989150
        # webauthn - support: supported
        # required_field_dc62:
        # timestamp: 1569245705824
        # timestamp_secret: 7b8b325c4f295029da8861463032808c5ff140b770d25f53c360651d896f72ea
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        # webauthn-support = 'supported'
        required_field_dc62 = ''
        timestamp = response.xpath("//input[@name='timestamp']/@value").extract_first()
        timestamp_secret = response.xpath("//input[@name='timestamp_secret']/@value").extract_first()
        post_data = dict(
            commit = commit,
            utf8 = utf8,
            authenticity_token=authenticity_token,
            # webauthn-support='supported'
            required_field_dc62=required_field_dc62,
            timestamp=timestamp,
            timestamp_secret=timestamp_secret,
            login = 'giant-xf',
            password = '819989150@163.com'
        )

        # print(post_data['commit'])
        yield scrapy.FormRequest(
            url='https://github.com/session',
            callback=self.after_login,
            formdata=post_data
        )

    def after_login(self,response):
        '''登入后处理'''
        # with open('a.txt','w',encoding="utf-8") as f:
        #     f.write(response.body.decode())
        print(re.findall(r"giant-xf",response.body.decode()))



