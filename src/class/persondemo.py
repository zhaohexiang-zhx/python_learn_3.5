#!/usr/bin/env python
# coding=utf-8

# 对象大写字母开头
class Person:

    # 初始化函数
    def __init__(self):
        # 定义类变量，各方法可共享，类的实例变量都要有self
        self.sex = ''

    def sex(self):
        pass

    def weight(self):
        pass

    def age(self):
        pass

    # 动作：将参数sex传入类变量
    def set_sex(self, sex):
        self.sex = sex

if __name__ == "__main__":
    amy_instance = Person()
    amy_instance.set_sex('女生')
    print(amy_instance.sex)
