#!/usr/bin/env python
# coding=utf-8

import time
from datetime import datetime
from datetime import timedelta

# 时间戳
def time_format():
    print(time.time())
    print(time.localtime())
    print(time.gmtime())
    # Y-2020,y-20
    print(time.strftime("%y %m %d %H:%M"))
    print(time.strftime("%y-%m-%d %H:%M:%S"))
    print(time.strftime("%c"))
    time_tuple = time.strptime("19 Feb 2021 1:30pm", "%d %b %Y %I:%M%p")
    print(type(time_tuple), time_tuple)
    print("分割线", "*"*40, "分割线")

# 时间
def datetime_format():
    print(datetime.now())
    print(datetime.utcnow())
    # strftime-格式化时间，strptime-字符串时间格式转换为时间
    print(datetime.now().strftime("%Y %m %d %H:%M"))
    date_format = datetime.now().strptime("19 Feb 2021 1:30pm", "%d %b %Y %I:%M%p")
    date = type(date_format)
    print(date, date_format)

# 时间差
def time_delta():
    d1 = datetime.strptime("2020-12-31 17:30:00", "%Y-%m-%d %H:%M:%S")
    d2 = datetime.strptime("2020-12-31 18:00:00", "%Y-%m-%d %H:%M:%S")
    delta = d2 - d1
    print(delta)

    # 三天后
    now = datetime.now()
    print(now)
    days_delta = timedelta(days=3)
    print(now+days_delta)

    # 三小时后
    hours_delta = timedelta(hours=3)
    print(now+hours_delta)

    # 3分钟后
    min_delta = timedelta(minutes=3)
    print(now+min_delta)





if __name__ == "__main__":
    # time_delta()
    # datetime_format()
    time_format()