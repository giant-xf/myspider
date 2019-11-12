# coding=utf-8
import pandas as pd
import numpy as np

# 将nan填充为均值
t1 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list("WXYZ")).astype(float)
t1['X'][1]=np.nan
print(t1)
# 自动给所在的列填充均值，无需定位
t1=t1.fillna(t1.mean())
print(t1.mean())
print(t1.fillna(t1.mean()))
print(t1)

# 将0填充为均值
t2 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list("WXYZ")).astype(float)
print(pd.isnull(t2))
print(pd.notnull(t2))
t2[t2==0]=t2.iloc[1:,0].mean()
print(t2)
