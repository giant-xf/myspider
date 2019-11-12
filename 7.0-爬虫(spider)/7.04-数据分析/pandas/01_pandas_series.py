# coding=utf-8
import numpy as np
import pandas as pd

t1 = np.arange(12).reshape(3,4)

print(t1)
t1 = pd.Series([11,22,33,44,23])
print(t1)
# 自创建索引
t1 = pd.Series([11,22,33,44,23],index=list('asdfg'))
print(t1)
# 使用字典创建
temp_dict = {'name':'xiaowang','age':18,'city':'shanghai'}
t1 = pd.Series(temp_dict)
print(t1)

print('-'*50)
# 获取其中的值
##
print(t1[['name','age']])
print(t1[1])
print(t1[:2])
## 一次取多个值还是一个object对象，还可以继续取
print(t1[[1,2]][1])
print('-'*50)
# 获取index和values

t2 = t1.index
for i in t2:
    print(i)
t3 = list(t2)
print(t3)

t2 = t1.values
for i in t2:
    print(i)
t3 = list(t2)
print(t3)