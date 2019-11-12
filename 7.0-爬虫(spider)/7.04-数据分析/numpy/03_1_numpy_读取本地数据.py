# coding=utf-8

import numpy as np

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
gb_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# frame:文件、字符串或生产器，
# dtype：数据类型，可选，决定CSV的字符串以什么数据类型读入数组中，默认np.float
# delimiter：分隔字符串，默认是任何空格，改为逗号
# skiprows:跳过前x行，一般跳过表头
# useccols: 读取指定行，索引，元组类型
# unpack：如果是True，读入属性将分别写入不同组变量，False服入数据只写入一个数组变量，默认False
# t1 = np.loadtxt(us_file_path,delimiter=',',dtype='int',unpack=1)
# t2 = np.loadtxt(gb_file_path,delimiter=',',dtype='int')
# print(t1)
# print(t2)
#
# # 数组转置的几种方法
# t3 = np.arange(4).reshape(2,2)
# t4 = t3.transpose()
# t5 = t4.T
# t6 = t5.swapaxes(1,0)
# print(t4)
# print(t5)
# print(t6)

print('*'*50)
# numpy各种取值方式
## 取行
### 单行
# print(t2[1])
# print(t2[2,:])
### 多行
# print(t2[1:,])
### 多行不连续
# print(t2[[1,3,4],])

## 取列
### 单列
# print(t2[:,1])
### 多列
# print(t2[:,2:])
### 多列不连续
# print(t2[:,[1,3]])

## 取多行多列交集
# print(t2[1:3,1:3])
## 取不连续的多行多列交集
# print(t2[[1,4,5],[0,3,3]])
## 去单行单列交集
# print(t2[1,3])


# numpy中数值的修改
t3 = np.arange(30).reshape(5,6)
## 直接修改某个值
# t3[3,3]=100
# print(t3)

## 将小于10的值都修改成0
### t3<10返回值是个bool类型的值
# print(t3<10)

# t3[t3<10]=0
# print(t3)

## 将小于10的值修改成0，将大于10的修改成10
# t4 = np.where(t3<10,0,10)
# print(t4)

## 将小于10的值修改成10，将大于18的值修改成18
# t5 = t3.clip(10,18)
# print(t5)

## nan型的值是float类型的,先修该类型在赋值
# t3 = t3.astype(float)
# t3[3,4]=np.nan
# print(t3)








