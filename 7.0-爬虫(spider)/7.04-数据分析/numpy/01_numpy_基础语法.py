# coding=utf-8
import numpy as np
import random

# 1.数组的基本的数据类型

# t1 = np.array([1,2,3,4])
# print(t1)
# print(t1.dtype)
#
# # 添加dtype确定数据类型
# t2 = np.array(range(10),dtype='int64')
# print(t2)
# print(t2.dtype)
#
# t3 = np.arange(1,10,2)
# print(t3)
# print(t3.dtype)
#
# # numpy 中的小数，使用round()方法取小数的精度
# t4 = np.array([np.random.random() for i in range(10)])
# print(t4)
# print(t4.dtype)
# t5 = np.array([round(random.random(),3) for i in range(10)])
# print(t5)
# print(t5.dtype)
#
# # 调整数据类型
# t6 = t5.astype('int8')
# print(t6.dtype)


# 2.多维数组的变化
t1 = np.array([1,2,3,4,5,6,])
 ## shape查看数组的维度,返回的是元组
print(t1.shape)

t2 = np.arange(12)
 ## reshape生成多维数组，也可以修改多维数组，返回值是多维数组
t3 = t2.reshape(3,4)
print(t3)

t4 = np.arange(24)
t5 = t4.reshape(2,3,4)
print(t5)

 ## 修该数组维度
t6 = t5.reshape(4,6)
print(t6)
 ## 变成一维数组
t7 = t5.reshape(24,)
print(t7)
t8 = t5.reshape((t5.shape[0]*t5.shape[1]*t5.shape[2]))
print(t8)
 ### 使用flatten直接修改成一维数组
t9 = t5.flatten()
print(t9)




