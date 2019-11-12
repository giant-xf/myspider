# coding=utf-8
import numpy as np

# 随机数种子，可以使系统每次生成相同的随机数
np.random.seed(1)

# 生成1以类随机数的多维数组
t1 = np.round(np.random.rand(2,3),3)
print(t1)

# 生成正态标准分布数据，平均值为0
t2 = np.random.randn(2,3)
print(t2)

# 生成给定范围内的随机整数，前面两个参数传范围，后面传入表示维度的元组(shape)
t3 = np.random.randint(1,10,(2,3))
print(t3)



