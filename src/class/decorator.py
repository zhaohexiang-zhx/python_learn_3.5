#!/usr/bin/env python
# coding=utf-8

# 装饰器 接受一个函数作为参数，然后返回一个新函数

import time
import random

def time_count(func):
    def wrap(*args, **kwargs):
        time_flag = time.time()
        temp_result = func(*args, **kwargs)
        print("time costs: ", time.time()-time_flag)
        return temp_result
    return wrap

@time_count

def loop_time(x, y):
    result = 0
    for i in range(x, y):
        time.sleep(random.choice(0.1, 0.2, 0.3))
        result = x + y
    return result

print(loop_time(1, 10))
print(loop_time(1, 10))
print(loop_time(1, 10))
# loop_time(1, 10)
# loop_time(1, 10)