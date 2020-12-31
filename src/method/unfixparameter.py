#!/usr/bin/env python
#coding=utf-8


def stu(profile, *mytuple):
    out_put = ""

    for parameter in mytuple:

        if not out_put:
            out_put = out_put + parameter
        else:
            out_put = out_put + "," + parameter
    return profile + ":" + out_put

print(stu("学生", "王二", "男", "100分"))


def stu1(profile, mytuple):
    out_put = ""

    for parameter in mytuple:
        if not out_put:
            out_put = out_put + parameter
        else:
            out_put = out_put + "," +parameter
    return profile + ":" + out_put

print(stu1("学生", ("王二", "男", "100分")))

