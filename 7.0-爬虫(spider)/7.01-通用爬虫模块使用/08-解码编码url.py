# python3中
from urllib import parse


str = '我是中国人'
print(str)
str1 = parse.quote(str)
print(str1)
str2 = parse.unquote(str1)
print(str2)

