#!/usr/bin/env python
# coding=utf-8

# 私有变量 __xxx 类内部可以访问，外部不能访问

class Person:

    total_person = 0
    def __init__(self, name, sex, province, weather):
        print("Init the class")
        self.__name = name
        self.sex = sex
        self.__province = province
        self._weather = weather

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_province(self, province):
        if province in ["Jilin", "Heilongjiang"]:
            return "Cold" + province
        else:
            return "Warm" + province

if __name__ == "__main__":

    per = Person("Xiaojingteng", "Male", "Taiwan", "Warm")
    print(per.sex)
    print(per._weather)
    # 此处不可直接访问 __name，可以通过调用方法get_name
    # print(per.__name)
    print(per.get_name())

