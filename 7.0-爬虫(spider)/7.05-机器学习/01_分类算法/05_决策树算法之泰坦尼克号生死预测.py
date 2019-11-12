# coding=utf-8
'''
决策树算法(相亲条件预测是否成功、泰坦尼克号预测、足球冠军预测)：

信息熵：信息熵越大表示越不确定，反正越确定。

决策树是按照信息增益排的。最大的在前根节点

ID3
信息增益 最大的准则
C4.5
信息增益比 最大的准则
CART 
回归树: 平方误差 最小 
分类树: 基尼系数   最小的准则 在sklearn中可以选择划分的原则

决策树的优缺点：
优点：
简单的理解和解释，树木可视化。
需要很少的数据准备，其他技术通常需要数据归一化，


缺点：
决策树学习者可以创建不能很好地推广数据的过于复杂的树，
        这被称为过拟合。
决策树可能不稳定，因为数据的小变化可能会导致完全不同的树
被生成


随机森林：在机器学习中，随机森林是一个包含多个决策树的分类器，并且其输出的类别是由个别树输出的类别的众数而定。

API：
class sklearn.ensemble.RandomForestClassifier(n_estimators=10, criterion=’gini’,
 max_depth=None, bootstrap=True, random_state=None)
随机森林分类器
n_estimators：integer，optional（default = 10） 森林里的树木数量
criteria：string，可选（default =“gini”）分割特征的测量方法
max_depth：integer或None，可选（默认=无）树的最大深度 
bootstrap：boolean，optional（default = True）是否在构建树时使用放回抽样 


随机森林的优点：
在当前所有算法中，具有极好的准确率
能够有效地运行在大数据集上
能够处理具有高维特征的输入样本，而且不需要降维
能够评估各个特征在分类问题上的重要性
对于缺省值问题也能够获得很好得结果


'''



from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def decision():
    """
    决策树对泰坦尼克号进行预测生死
    :return: None
    """
    # 获取数据
    titan = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")

    # 处理数据，找出特征值和目标值
    x = titan[['pclass', 'age', 'sex']]

    y = titan['survived']

    print(x)
    # 缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True)

    # 分割数据集到训练集合测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 进行处理（特征工程）特征-》类别-》one_hot编码
    dict = DictVectorizer(sparse=False)

    x_train = dict.fit_transform(x_train.to_dict(orient="records"))

    print(dict.get_feature_names())

    x_test = dict.transform(x_test.to_dict(orient="records"))

    # print(x_train)
    # 用决策树进行预测
    # dec = DecisionTreeClassifier()
    #
    # dec.fit(x_train, y_train)
    #
    # # 预测准确率
    # print("预测的准确率：", dec.score(x_test, y_test))
    #
    # # 导出决策树的结构
    # export_graphviz(dec, out_file="./tree.dot", feature_names=['年龄', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', '女性', '男性'])

    # 随机森林进行预测 （超参数调优）
    rf = RandomForestClassifier()

    param = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}

    # 网格搜索与交叉验证
    gc = GridSearchCV(rf, param_grid=param, cv=2)

    gc.fit(x_train, y_train)

    print("准确率：", gc.score(x_test, y_test))

    print("查看选择的参数模型：", gc.best_params_)

    return None


if __name__ == '__main__':
    decision()