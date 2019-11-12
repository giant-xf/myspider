# coding=utf-8

import numpy as np

# 二维:
t1 = np.arange(12)
t1 = t1.reshape(3,4)

t2 = np.arange(4)
# print(t1*t2)
# print(t1/t2)
print(t1+t2)
print(t1-t2)
print('-'*50)
# 多维数组
t3 = np.arange(24).reshape(2,3,4)

t4 = np.arange(3).reshape(1,3,1)

# print(t3*t4)
# print(t3/t4)
print(t3)
print(t4)
print(t3+t4)
# print(t3-t4)



