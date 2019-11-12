# coding=utf-8
import pandas as pd
import numpy as np

t1 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('WXYZ'))
print(t1)
# 根据名字索引
# print(t1['W'])
# print(t1[:2])

# todo:通过标签获取数据loc()
# 取列
print(t1.loc[:,['W','X']])
# 取行
print(t1.loc[['a'],:])
# 取行和列的交集
print(t1.loc[['a','b'],['W','X']])

print('-'*100)
# todo:通过位置获取数据
print(t1.iloc[:2,:2])
print(t1.iloc[[1,2],[2,3]])

# 给某些数据赋值
t1.iloc[:2,:3] = 100
print(t1)

# 可以给其直接赋nan，自动转变类型
t1.iloc[:2,1] = np.nan
print(t1.dtypes)
'''
W      int32
X    float64
Y      int32
Z      int32
'''

