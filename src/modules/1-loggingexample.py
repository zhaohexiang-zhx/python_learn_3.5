#!/usr/bin/env python
# coding=utf-8

import logging
from logging.handlers import RotatingFileHandler

def log_basic():
    # CRITICAL 50; ERROR 40; WARNING 30; INFO 20; DEBUG 10; NOSET 0;
    # filename-指定日志输出文件的文件名; format-指定日志格式字符串，
    logging.basicConfig(filename="1-web.log", level=0,
                        format='%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    logging.getLogger("paramiko").setLevel(logging.WARNING)
    logging.getLogger("selenium").setLevel(logging.WARNING)

    logging.debug("this is debug log")
    logging.info("test info log")

def log_rorate():
    format = '%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s'
    logging.basicConfig(level=20, format='%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')

    # 定义RotatingFileHandler，且文件大小超过10M时进行备份，最多5个备份日志文件
    rotateHandler = RotatingFileHandler('1-you.log', maxBytes=1024 * 0.01, backupCount=5)
    rotateHandler.setFormatter(logging.Formatter(format))
    logging.getLogger("").addHandler(rotateHandler)
    logging.getLogger().propagate = False

    logging.info("my log"*50)

if __name__ == "__main__":
    # log_basic()
    log_rorate()