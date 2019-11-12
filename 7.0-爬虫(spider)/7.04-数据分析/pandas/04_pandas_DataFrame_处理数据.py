# coding=utf-8
from pymongo import MongoClient
import pandas as pd

# client = MongoClient()
# collection = client["douban"]["tv1"]
# data = collection.find()
# data_list = []
# for i in data:
#     temp = {}
#     temp["info"]= i["info"]
#     temp["rating_count"] = i["rating"]["count"]
#     temp["rating_value"] = i["rating"]["value"]
#     temp["title"] = i["title"]
#     temp["country"] = i["tv_category"]
#     temp["directors"] = i["directors"]
#     temp["actors"] = i['actors']
#     data_list.append(temp)
# t1 = data[0]
# t1 = pd.Series(t1)
# print(t1)

# df = pd.DataFrame(data_list)
# print(df)

#显示头几行
# print(df.head(1))
# print("*"*100)
# print(df.tail(2))

#展示df的概览
# print(df.info())
# print(df.describe())
# print(df["info"].str.split("/").tolist())

t1 = pd.read_csv("./dogNames2.csv")
# print(t1)
t2 = t1.sort_values(by='Count_AnimalName')
print(t2)
# print(t1.shape)
# print(t1.dtypes)
# print(t1.ndim)
# print(t1.index)
# print(t1.values)
# print(t1.info())
# print(t1.describe())
print(t2[:20]['Count_AnimalName'])
print(t2["Count_AnimalName"][:20])


'''
# 排序，根据指定的by字段排序，ascending默认为True为从小到大，
df.sort_values(by="Count_AnimalName",ascending=False)

df.shape    # 行数 列数
df.dtypes   # 每列数据类型
df.ndim     # 数据维度
df.index    # 行索引
df.columns  # 列索引
df.values   # 对象值，二维ndarray数组

df.head()   # 显示头几行，默认显示5行
df.tail()   # 显示后几行，默认5行
df.info()   # 相关信息概览，行数、列数等等一些信息
df.describe()   # 快速综合统计结果:计数、均值、极差、方差等信息
'''