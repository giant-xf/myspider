# coding=utf-8

from matplotlib import pyplot as plt
import matplotlib

# 修改字体，使其能显示中文
font = {'family':'MicroSoft YaHei',
        'weight':'bold'
        }
matplotlib.rc("font",**font)

x = range(11,31)
y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]

_xtick_labels = ['{}岁'.format(i) for i in range(11,31)]

plt.xticks(x,_xtick_labels,rotation=45)
plt.yticks(y)


plt.xlabel("年龄")
plt.ylabel("个数")
plt.title("每年龄阶段交女朋友的数量")

plt.plot(x,y)
plt.show()


