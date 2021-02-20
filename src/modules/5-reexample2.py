#!/usr/bin/env python
# coding=utf-8

import re

# \d,匹配数字
p = re.compile(r'\d+')
print(p.findall('fhaksd1jhsdk2jhk3jhk5'))
