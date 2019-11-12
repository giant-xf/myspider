# coding=utf-8

from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# 第一种方式：
# 修改字体，使其能显示中文
font = {'family':'MicroSoft YaHei',
        'weight':'bold'
        }
matplotlib.rc("font",**font)

# 第二种方式：
# my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\PingFang.ttc")

# x = range(2,26,2)
x = range(0,120)

y = [random.randint(20,35) for i in range(120)]

# 设置界面大小
plt.figure(figsize=(13,8),dpi=80)

# 绘图
plt.plot(x,y)

# 设置刻度,将其截取的值范围越小，x轴上面的点越密集
# _xtick_labels = [i/2 for i in range(4,49)]
# 设置刻度,将其截取的值范围越大，x轴上面的点越分散
# _xtick_labels = [i/2 for i in range(4,49,3)]
# plt.xticks(_xtick_labels)

_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]

# plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,FontProperties=my_font) # rotation旋转的角度
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45)

# _ytick_labels = [i for i in range(min(y),max(y)+1)]
# plt.yticks(_ytick_labels)

# 将图片保存，svg图片矢量不失帧
# plt.savefig("./a.svg")

# 添加描述信息
plt.xlabel("时间")
plt.ylabel("气温")
plt.title("10点到12点每分钟的气温变化")

plt.grid(alpha=0.4,linestyle='--')
plt.show()




