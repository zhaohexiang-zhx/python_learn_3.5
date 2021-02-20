#!/usr/bin/env python
# coding=utf-8


import re

# 将正则表达式编译层Pattern对象
pattern = re.compile(u'你好')

# 使用Pattern匹配文本，获取匹配结果，无法匹配时将返回None

# str = pattern.match(u'，世界！')

# match（）开始的字符匹配不上，返回none
str = pattern.search(u'  你好')

# search()可以
# str = pattern.search(u'    你好')

print(str)
if str:
    # 使用Match获得分组信息
    print("result: ", str.group())
