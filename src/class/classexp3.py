#!/usr/bin/env python
# coding=utf-8

from classexp1 import Person

# 继承父类Person
class Student(Person):

    def __init__(self, name, sex, province, grade):
        # super(Student, self).__init__(name, sex, province)
        Person.__init__(self, name, sex, province)
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return "不告诉你名字"

    def get_nick_name(self):
        name = Person.get_name(self)
        if name.startswith("小"):
            return name.replace("小", "小小")
        else:
            return name



if __name__ == "__main__":
    stu = Student("小赵", "Female", "Beijing", 6)
    # get_name()方法子类中有，就访问子类的方法，子类中没有，去访问父类的方法
    # print(stu.get_name())
    print(stu.get_nick_name())
