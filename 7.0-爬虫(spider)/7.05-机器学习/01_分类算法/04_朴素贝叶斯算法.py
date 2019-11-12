# coding=utf-8
# todo:朴素贝叶斯算法
"""
朴素贝叶斯算法常用于文本分类(垃圾邮箱分类)

公式：P(C|W)=P(W|C)P(C)/P(W)
公式分为三个部分：
P(C)：每个文档类别的概率(某文档类别词数／总文档词数)

P(W│C)：给定类别下特征（被预测文档中出现的词）的概率

P(F1,F2,…)     预测文档中每个词的概率 

解决方法：拉普拉斯平滑系数

P(F1│C)=(Ni+1)/(N+am)   a为指定的系数一般为1，m为训练文档中统计出的特征词个数

朴素贝叶斯接口api:       
sklearn.naive_bayes.MultinomialNB(alpha = 1.0)
朴素贝叶斯分类
alpha：拉普拉斯平滑系数

优点：
1.朴素贝叶斯模型发源于古典数学理论，有稳定的分类效率。
2.对缺失数据不太敏感，算法也比较简单，常用于文本分类。
3.分类准确度高，速度快

缺点：
1.需要知道先验概率P(F1,F2,…|C)，因此在某些时候会由于假设的先验模型的原因导致预测效果不佳。



"""

from sklearn.datasets import  fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report




def naviebayes():
    """
    朴素贝叶斯进行文本分类
    :return: None
    """
    news = fetch_20newsgroups(subset='all')

    # 进行数据分割
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)

    # 对数据集进行特征抽取
    tf = TfidfVectorizer()

    # 以训练集当中的词的列表进行每篇文章重要性统计['a','b','c','d']
    x_train = tf.fit_transform(x_train)

    print(tf.get_feature_names())

    x_test = tf.transform(x_test)

    # 进行朴素贝叶斯算法的预测
    mlt = MultinomialNB(alpha=1.0)

    # print(x_train.toarray())

    mlt.fit(x_train, y_train)

    y_predict = mlt.predict(x_test)

    print("预测的文章类别为：", y_predict)

    # 得出准确率
    print("准确率为：", mlt.score(x_test, y_test))

    print("每个类别的精确率和召回率：", classification_report(y_test, y_predict, target_names=news.target_names))

    # precision精度    recall召回  f1-score准确度   support符合的样本数

    return None


if __name__ == "__main__":
    naviebayes()
