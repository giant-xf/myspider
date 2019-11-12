# coding=utf-8

import pandas as pd
import numpy as np

t1 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('WXYZ'))
# print(t1)
t2 = pd.DataFrame(np.zeros((2,3)),index=['a','d'],columns=list('wxy'))
t2.iloc[1,0]=1
print(t1)
print(t2)

# join: 谁在前就以谁为准来合并，没有的数据用NaN来补充
# t3 = t1.join(t2)
# print(t3)
# t3 = t2.join(t1)
# print(t3)

# merge: inner为交集,outer为并集
# t3 = t1.merge(t2,left_on='W',right_on='w',how='inner')
# print(t3)

# t3 = t1.merge(t2,left_on='W',right_on='w',how='outer')
# print(t3)

t3 = t1.merge(t2,left_on='W',right_on='w',how='left')
print(t3)

t3 = t1.merge(t2,left_on='W',right_on='w',how='right')
print(t3)