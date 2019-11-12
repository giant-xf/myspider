# coding=utf-8

import numpy as np
from matplotlib import pyplot as plt
import matplotlib
# 修改字体，使其能显示中文
font = {'family':'MicroSoft YaHei',
        'weight':'bold'
        }
matplotlib.rc("font",**font)

us_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

us_video_data = np.loadtxt(us_file_path,delimiter=',',dtype=int)

# print(uk_video_data)

us_comments = us_video_data[:,-1]

us_comments = us_comments[us_comments<=5000]
print(us_comments.max(),us_comments.min())

d = 250

bin_nums = (us_comments.max()-us_comments.min())//d

# 绘制
plt.figure(figsize=(10,7),dpi=80)
plt.hist(us_comments,bin_nums)

# 添加描述信息
plt.xlabel('评论数')
plt.ylabel('电影数')
plt.title('评论数对应的电影数')

plt.show()




