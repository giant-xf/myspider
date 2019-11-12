# coding=utf-8

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file_path = './IMDB-Movie-Data.csv'

df = pd.read_csv(file_path)
print(df['Genre'].head(3))

# 统计分类的列表
temp_list = df['Genre'].str.split(",").tolist()  #[[],[],[]]
# 使用集合去重，
genre_list = list(set(i for j in temp_list for i in j))
print(genre_list)

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
# print(zeros_df)

# 给每个电影出现分类的位置赋值1
for i in range(df.shape[0]):
    zeros_df.loc[i,temp_list[i]]=1

# print(zeros_df)

# 统计个数
genre_count = zeros_df.sum(axis=0)
print(genre_count)

# 排序
genre_count = genre_count.sort_values()

plt.figure(figsize=(10,7),dpi=80)

_x = genre_count.index
_y = genre_count.values

# 绘制图
plt.bar(range(len(_x)),_y)
# 给x轴添加刻度
plt.xticks(range(len(_x)),_x,rotation=45)

plt.grid(alpha=0.2)

plt.show()






