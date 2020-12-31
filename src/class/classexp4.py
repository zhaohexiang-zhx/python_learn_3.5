#!/usr/bin/env python
# coding=utf-8

#多重继承

from classexp3 import Student

class SeniorStudent(Student):

    def __init__(self, name, sex, province, grade):

        Student.__init__(self, name, sex, province, grade)
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return "不告诉你Senior名字"

    def overtime_study(self):
        if self.grade == 3:
            return "补课"
        else:
            return "玩"

if __name__ == "__main__":
    stu1 = SeniorStudent("小鹏", "男", "山东", 4)
    print(stu1.overtime_study())
    print(stu1.get_name())


