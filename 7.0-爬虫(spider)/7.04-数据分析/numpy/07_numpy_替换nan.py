# coding=utf-8
import numpy as np


# print(t1)
def fill_ndarray(t1):
    for i in range(t1.shape[1]):    # 遍历每一列
        temp_col = t1[:,i]  # 当前的每一列
        # print(temp_col)
        # print(temp_col!=temp_col)
        nan_num = np.count_nonzero(temp_col!=temp_col)  # 统计那一列中有nan
        # print(nan_num)
        if nan_num!=0:  # 说明这一列中有nan
            temp_not_nan_col = temp_col[temp_col==temp_col]    # 当前一列不为nan的数组
            # print(temp_not_nan_col)
            temp_mean = temp_not_nan_col.mean()     # 求不为nan数组的平均值
            # temp_col[temp_col != temp_col] = temp_mean  # 将平均值赋值给为nan的值
            temp_col[np.isnan(temp_col)] = temp_mean
    return t1

if __name__ == '__main__':
    t1 = np.arange(12).reshape(3, 4).astype(float)
    t1[1, 1:3] = np.nan
    t1 = fill_ndarray(t1)
    print(t1)
