from selenium import webdriver
import time


class DouyuSpider(object):
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.binary_location = r'D:\谷歌浏览器\Google\Chrome\Application\chrome.exe'
        self.driver = webdriver.Chrome(chrome_options=self.option)
        self.start_url = "https://www.douyu.com/directory/all"

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@class='layout-Cover-list']/li")
        content_list = []
        for li in li_list:
            item ={}
            item["room_img"] = li.find_element_by_xpath(".//img[@class='DyImg-content is-normal']").get_attribute("src")
            item["room_fenlei"] = li.find_element_by_xpath(".//h3[@class='DyListCover-intro']").get_attribute("title")
            item["room_title"] = li.find_element_by_xpath(".//h3[@class='DyListCover-intro']").get_attribute("title")
            item['anchor_name'] = li.find_element_by_xpath(".//h2[@class='DyListCover-user']").text
            item["room_hot"] = li.find_element_by_xpath(".//span[@class='DyListCover-hot']").text
        next_url = self.driver.find_elements_by_xpath(".//span[@class='dy-Pagination-item-custom']")
        next_url = next_url[0] if len(next_url)>0 else None
        print(item)
        content_list.append(item)
        return content_list, next_url

    def save_content_list(self,content_list):
        with open('斗鱼房间信息/douyu.txt','w', encoding='urf-8') as f:
            f.write(content_list)
        print('保存成功')
    def run(self):
        # 1.star_url
        # 2.发送请求
        self.driver.get(self.start_url)
        # 3.提取数据，提取下一页元素
        content_list, next_url = self.get_content_list()
        # 4.保存数据
        self.save_content_list(content_list)
        # 5.点击下一页元素，进入循环
        while next_url is not None:
            next_url.click()
            content_list, next_url = self.get_content_list()
            self.save_content_list()



if __name__ == '__main__':
    douyu = DouyuSpider()
    douyu.run()


