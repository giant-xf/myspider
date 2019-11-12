# coding=utf-8
from matplotlib import pyplot as plt
import matplotlib

# 修改字体，使其能显示中文
font = {'family':'MicroSoft YaHei',
        'weight':'bold'
        }
matplotlib.rc("font",**font)

# 设置图形大小
plt.figure(figsize=(13,8),dpi=80)

interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

# 绘制条形图,当width=1的时候，两个条形图会连在一起
plt.bar(range(len(interval)),quantity,width=1)

# 设置x轴的刻度
_x = [ i-0.5 for i in range(len(interval)+1)]
_xtick_labels = interval+[150]
plt.xticks(_x,_xtick_labels)

plt.grid()
plt.show()





