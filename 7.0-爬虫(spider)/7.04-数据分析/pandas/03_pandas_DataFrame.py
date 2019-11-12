# coding=utf-8

import pandas as pd
import numpy as np

# DataFrame是一个二维的
# DataFrame对象既有行索引，又有列索引
# 行索引，表明不同行，横向索引，叫index，0轴，axis=0
# 列索引，表名不同列，纵向索引，叫columns，1轴，axis=1
# 是以Series为容器
# t1 = pd.DataFrame(np.arange(12).reshape(3,4))
# print(t1)

# 给DataFrame指定行和列
# t1 = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("MNOP"))
# print(t1)


# 给DataFrame传入字典数据,
## 字典里面嵌套列表,不够的数据自动补全为nan
data_dict = {'name':['laowang','laozhang'],'age':[22,12],'tel':[10010,10086]}
t1 = pd.DataFrame(data_dict)
print(t1)
## 结果
'''
       name  age    tel
0   laowang   22  10010
1  laozhang   12  10086
'''

## 列表里面嵌套字典,不够的数据自动补全为nan
data_dict = [{'name':'laowang',"age":18,'tel':10010},{'name':'laosi','age':22},{"name":'laozhang','tel':10086}]
t1 = pd.DataFrame(data_dict)
print(t1)
## 结果
'''       name   age      tel
0   laowang  18.0  10010.0
1     laosi  22.0      NaN
2  laozhang   NaN  10086.0
'''



