
from lxml import etree


text = ''' <div><ul> 
    <li class="item-1"><a href="link1.html"></a></li> 
    <li class="item-1"><a href="link2.html">second item</a></li> 
    <li class="item-inactive"><a href="link3.html">third item</a></li> 
    <li class="item-1"><a href="link4.html">fourth item</a></li> 
    <li class="item-0"><a href="link5.html">fifth item</a>
    </ul> </div> '''

html = etree.HTML(text)
print(type(html))
print(html)
# 查看element对象包含的字符串
# ret1 = etree.tostring(html)
# print(ret1.decode())

# 获取class为item-1 li下的a的href
ret1 = html.xpath('//li[@class="item-1"]/a/@href')
print(ret1)
# 获取class为item-1 li下的a的文本
ret2 = html.xpath('//li[@class="item-1"]/a/text()')
print(ret2)

print('-'*50)

# 将标题和网址组成。会出现一个问题，如果某一个没有标题，或者没有网址，就会出现网址和标题不匹配。
# for href in ret1:
#     dict = {}
#     dict['href'] = href
#     dict['title'] = ret2[ret1.index(href)]
#     print(dict)

# 该类型是element对象
ret3 = html.xpath('//li[@class="item-1"]')
print(ret3)


for ret in ret3:
    dict = {}
    # ret.xpath(''./a/@href是列表类型，只有一个数据
    dict['href'] = ret.xpath('./a/@href')[0] if len(ret.xpath('./a/@href'))>0 else None
    dict['title'] = ret.xpath('./a/text()')[0] if len(ret.xpath('./a/text()'))>0 else None
    print(dict)




