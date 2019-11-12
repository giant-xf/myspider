# coding=utf-8
import numpy as np

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
gb_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

t1 = np.loadtxt(us_file_path,delimiter=',',dtype='int')
t2 = np.loadtxt(gb_file_path,delimiter=',',dtype='int')

# 全是0的多维数组,默认是float类型，传入的元组表示几行几列
zero_data = np.zeros((t1.shape[0],1),dtype='int')
one_data = np.ones((t2.shape[0],1),dtype='int')

# print(zero_data)
# print(one_data)

# 数组的拼接，np.vstack((t1,t2))---->竖直拼接。np.hstack((t1,t2))---->水平拼接
# 必须传入的是元组，拼接的顺序由传入的值顺序决定
t1 = np.hstack((t1,zero_data))
t2 = np.hstack((t2,one_data))
t1_t2 = np.vstack((t1,t2))
print(t1_t2)

print("-"*50)
# 创建对角线为1的方阵
t3 = np.eye(4)
print(t3)

# 找出数组中最大值的位置
t4 = np.argmax(t3,axis=0)
print(t4)

# 将对角线上的值换成-1
print(t3==1)
t3[t3==1]=-1

# 找出数组中最小值的位置
t5 = np.argmin(t3,axis=1)
print(t5)

print('-'*50)
# 行列交换
tt = np.arange(12).reshape(3,4)
print(tt)
tt[[1,2],:] = tt[[2,1],:]
print(tt)


