# 基本语法
# from lxml import etree
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li/a/text()')
# /表示子节点，//表示子孙节点，@表示属性，*表示任意节点，..表示父节点，属性多个值可以用 contains,多属性可以用and等运算符
# 其他运算符：or, +.,-,*,div,mod, >, <
# 索引的使用：数字索引[1], 最后一个[last()],倒数第3个[last()-2],位置前后[position()<3],
print(result)

# text = '''  
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''  
# # from lxml import etree

# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class,"li") and @name = "item"]/a/text()')
# print(result)