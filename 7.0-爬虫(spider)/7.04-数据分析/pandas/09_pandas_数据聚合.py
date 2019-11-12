# coding=utf-8
import pandas as pd
import numpy as np

file_path = './starbucks_store_worldwide.csv'

df = pd.read_csv(file_path)

# print(df.head(1))
print(df.info())

# 以Country进行分组。
grouped = df.groupby(by='Country')
print(grouped)

## 遍历grouped
# 得到的数据是一个元组。是以分组的条件为元组第一元素，其他的为第二元素
# for i,j in grouped:
#     print(i)
#     print('-'*100)
#     print(j)


# print(grouped.count()['Brand'])

# 计算出每个国建的所有的星巴克的数量
# us_count = grouped.count()['Brand']['US']
# cn_count = grouped.count()['Brand']['CN']
# print(us_count)
# print(cn_count)

# 计算中国每个省的星巴克数量
china_data = df[df["Country"]=='CN']
cn_state_count = china_data.groupby(by='State/Province').count()['Brand']

print(cn_state_count)