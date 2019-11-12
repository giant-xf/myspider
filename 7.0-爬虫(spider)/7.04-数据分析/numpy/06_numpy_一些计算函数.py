# coding=utf-8
import numpy as np

np.random.seed(1)
t1 = np.random.randint(10,100,(3,4))
# 将t1装换吃你个float类型
t1 = t1.astype(float)
t1[1,2]=np.nan
print(t1)

# print(np.nan == np.nan)
# print(t1!=t1)
# # 判断整个t1中是否有为nan值
# print(np.isnan(t1))
#
# # copy可以拷贝t1的值，互不影响
# t2 = np.copy(t1)
# t2[:,0] = 0
# print(t2)
# # 打印不是0的值的个数
# print('不为0的个数:{}'.format(np.count_nonzero(t2)))

# 计算求和函数
## 只要有一个值为nan，整个值都为nan
s1 = t1.sum()
print(s1)

## 求行或者列的所有值,axis=0表示求竖向求值，axis=1表示横向求值
s2 = t1.sum(axis=0)
print(s2)
s3 = t1.sum(axis=1)
print(s3)

print('-'*50)

# 求平均值,axis=0表示求竖向求值，axis=1表示横向求值
mean1 = t1.mean(axis=0)
mean1 = np.round(mean1,2)
print(mean1)
mean2 = t1.mean(axis=1)
mean2 = np.round(mean2,2)
print(mean2)

print('-'*50)
# 求中值(中间值),中间大小的那个值,axis=0表示求竖向求值，axis=1表示横向求值
median1 = np.median(t1,axis=0)
print(median1)
median2 = np.median(t1,axis=1)
print(median2)

print('-'*50)
# 求最大值和最小值，axis=0表示求竖向求值，axis=1表示横向求值
max1 = t1.max(axis=0)   # min求最小值
print(max1)
max2 = t1.max(axis=1)   # min求最小值
print(max2)

print('-'*50)
# 求极值(最大值和最小值差)和标准差(方差(每个值减去平均值的平方的平均数)),
p1 = np.ptp(t1,axis=0)
print(p1)
p2 = t1.std(axis=0)
print(p2)

# 给nan填充均值
## 填充为每一列的均值

## 填充为每一行的均值



