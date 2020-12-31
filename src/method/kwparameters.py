#!/usr/bin/env python
#coding=utf-8

def add(x, **kwargs):
    total = x
    for arg, value in kwargs.items():
        print("adding", arg)
        total += value
    return total
grade = add(10, y=11, z=12, m=13, n=14)
print(grade)