# coding=utf-8
import numpy as np
from matplotlib import  pyplot as plt

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t_uk = np.loadtxt(uk_file_path,delimiter=",",dtype="int")

#选择喜欢数比50万小的数据
t_uk = t_uk[t_uk[:,1]<=500000]

print(t_uk)
t_uk_comment = t_uk[:,-1]
print(t_uk_comment)
t_uk_like = t_uk[:,1]



plt.figure(figsize=(10,7),dpi=80)
# 以喜欢数为x轴，以评论数为y轴
plt.scatter(t_uk_like,t_uk_comment)

plt.show()