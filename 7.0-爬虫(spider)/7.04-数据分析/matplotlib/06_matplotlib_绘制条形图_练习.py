# coding=utf-8
from matplotlib import pyplot as plt
import matplotlib

# 修改字体，使其能显示中文
font = {'family':'MicroSoft YaHei',
        'weight':'bold'
        }
matplotlib.rc("font",**font)

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

# 设置图形大小
plt.figure(figsize=(13,8),dpi=80)

bar_width = 0.2

x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width for i in x_15]

plt.bar(x_14,b_14,width=bar_width,label='14号')
plt.bar(x_15,b_15,width=bar_width,label='15号')
plt.bar(x_16,b_16,width=bar_width,label='16号')
# 设置图例
plt.legend()

# 设置x轴刻度
plt.xticks(x_15,a)

# 添加描述信息
plt.xlabel("电影名")
plt.ylabel("票房")
plt.title("连续三天各电影票房情况")

plt.show()


