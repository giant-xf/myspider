# coding=utf-8
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import pandas as pd

# 使用加载器读取数据并且存入变量iris
lr = load_iris()

# 查验数据规模
# print(iris.data.shape)

# 查看数据说明（这是一个好习惯）
# print (lr)

# 对Iris数据集进行分割,0.25的训练集，0.75的测试集
# random_state：可以为整数、RandomState实例或None，默认为None
#   ①若为None时，每次生成的数据都是随机，可能不一样
#   ②若为整数时，每次生成的数据都相同
x_train, x_test, y_train, y_test =train_test_split(lr.data,lr.target,test_size=0.25,random_state=None)

# 进行标准化
std = StandardScaler()
# 对数据的训练集和测试集进行标准化
x_train = std.fit_transform(x_train)
x_test = std.fit_transform(x_test)

# 实例化K-近邻算法对象
knn = KNeighborsClassifier()

# fit， predict,score
knn.fit(x_train, y_train)

# 得出预测结果
y_predict = knn.predict(x_test)

print("预测的花的产地为：", y_predict)

# 得出准确率
print("预测的准确率:", knn.score(x_test, y_test))

