# coding=utf-8

import pandas as pd
from pymongo import MongoClient

# 读取csv文件
# df = pd.read_csv('./dogNames2.csv')
# print(df)

# 处理mongodb数据
client = MongoClient(host="192.168.43.150",port=27017)
collection = client["yangguang"]["xinxi"]
data = list(collection.find())

t1 = data[0]
t1 = pd.Series(t1)
print(t1)







