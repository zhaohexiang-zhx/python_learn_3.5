#!/usr/bin/env python
# coding=utf-8

# 有构造函数：在函数初始化时，已知道所有变量

class Person(object):

    # 类变量，全局变量
    total_person = 0

    # 构造函数  self实例对象
    def __init__(self, name, sex, score):
        print("Init the class")
        # 实例变量，为了使在各个方法中能够共享
        self.name = name
        self.sex = sex
        self.score = score
        # 类变量，通过“类名.变量名”访问
        Person.total_person += 1

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex


if __name__=="__main__":
    person1 = Person("xiaowang", "Male", "shandong")
    print(person1.name)
    print(person1.sex)
    print(person1.get_name())
    print(person1.get_sex())
    print(person1.total_person)
    print("*" * 50)

    person2 = Person("xiaozhao", "Female", "beijing")
    print(person2.name)
    print(person2.total_person)
