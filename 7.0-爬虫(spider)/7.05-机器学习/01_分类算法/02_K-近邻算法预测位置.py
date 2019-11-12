# coding=utf-8

# todo:k-近邻算法
'''
k-近邻算法是对需要预测的数据与已给的数据根据公式进行距离计算.

所给的值还需进行处理：添加特征值、删除特征值等操作，
***还需进行标准化处理

两个样本的距离可以通过如下公式计算，又叫欧式距离
比如说，a(a1,a2,a3),b(b1,b2,b3)
公式:
根号下((a1-b1)^2+(a2-b2)^2+(a3-b3)^2)

1、k值取多大？有什么影响？
k值取很小：容易受异常点影响
k值取很大：容易受最近数据太多导致比例变化

# 流程：
1、数据集的处理
2、分割数据集
3、对数据集进行标准化
4、estimator流程进行分类预测

优点：
简单，易于理解，易于实现，无需估计参数，无需训练

缺点：
懒惰算法，对测试样本分类时的计算量大，内存开销大
必须指定K值，K值选择不当则分类精度不能保证

模型的选择与调优:
1、交叉验证：为了让被评估的模型更加准确可信；
将拿到的数据，分为训练和验证集。以下图为例：将数据分
成5份，其中一份作为验证集。然后经过5次(组)的测试，每次都更换不同
的验证集。即得到5组模型的结果，取平均值作为最终结果。又称5折交叉
验证。

2、网格搜索



'''

from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


# li = load_iris()

# print("获取特征值")
# print(li.data)
# print("目标值")
# print(li.target)
# print(li.DESCR)

# 注意返回值, 训练集 train  x_train, y_train        测试集  test   x_test, y_test
# test_size :样本占比，如果是整数的话就是样本的数量
# x_train, x_test, y_train, y_test = train_test_split(li.data, li.target, test_size=0.25)
#
# print("训练集特征值和目标值：", x_train, y_train)
# print("测试集特征值和目标值：", x_test, y_test)

# news = fetch_20newsgroups(subset='all')
#
# print(news.data)
# print(news.target)
#
# lb = load_boston()
#
# print("获取特征值")
# print(lb.data)
# print("目标值")
# print(lb.target)
# print(lb.DESCR)


def knncls():
    """
    K-近邻预测用户签到位置
    :return:None
    """
    # 读取数据
    data = pd.read_csv("./data/FBlocation/train.csv")

    # print(data.head(10))

    # 处理数据
    # 1、缩小数据,查询数据筛选
    data = data.query("x > 1.0 &  x < 1.25 & y > 2.5 & y < 2.75")

    # 处理时间的数据,默认为秒
    time_value = pd.to_datetime(data['time'], unit='s')

    print(time_value)

    # 把日期格式转换成 字典格式
    time_value = pd.DatetimeIndex(time_value)

    # 构造一些特征
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday

    # 把时间戳特征删除
    data = data.drop(['time'], axis=1)

    print(data)

    # 把签到数量少于n个目标位置删除
    place_count = data.groupby('place_id').count()

    tf = place_count[place_count.row_id > 3].reset_index()

    data = data[data['place_id'].isin(tf.place_id)]

    # 取出数据当中的特征值和目标值
    y = data['place_id']

    x = data.drop(['place_id'], axis=1)

    # 进行数据的分割训练集合测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 特征工程（标准化）
    std = StandardScaler()

    # 对测试集和训练集的特征值进行标准化
    x_train = std.fit_transform(x_train)

    x_test = std.fit_transform(x_test)

    # 进行算法流程 # 超参数
    knn = KNeighborsClassifier()

    # # fit， predict,score
    # knn.fit(x_train, y_train)
    #
    # # 得出预测结果
    # y_predict = knn.predict(x_test)
    #
    # print("预测的目标签到位置为：", y_predict)
    #
    # # 得出准确率
    # print("预测的准确率:", knn.score(x_test, y_test))

    # 构造一些参数的值进行搜索，进行交叉验证
    param = {"n_neighbors": [3, 5, 10]}

    # 进行网格搜索
    gc = GridSearchCV(knn, param_grid=param, cv=2)

    gc.fit(x_train, y_train)

    # 预测准确率
    print("在测试集上准确率：", gc.score(x_test, y_test))

    print("在交叉验证当中最好的结果：", gc.best_score_)

    print("选择最好的模型是：", gc.best_estimator_)

    print("每个超参数每次交叉验证的结果：", gc.cv_results_)

    return None

if __name__ == '__main__':
    knncls()










