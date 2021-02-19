#!/usr/bin/env python
# coding=utf-8

import codecs
import time


def open_example(in_file):
    '''
    r:read
    向已有内容的文件中添加，使用a，若用w，会删除原有内容
    a:append
    w:write
    '''
    file_instance = open(in_file, "r")
    content = file_instance.read()
    file_instance.close()
    print(content)


def open_utf8(in_file):
    file_instance = codecs.open(in_file, "r", encoding='UTF-8')
    content = file_instance.read()
    file_instance.close()
    print(content)

def write_utf8(in_file):
    file_instance = codecs.open(in_file, "a", encoding='UTF-8')
    file_instance.write(u'新的一行' + '\n')
    file_instance.write(u'新的二行' + '\n')
    file_instance.writelines([u'新的三行' + '\n', u'新的四行' + '\n'])

    file_instance.flush()
    print('I am sleeping')

    time.sleep(10)
    file_instance.close()


if __name__ == "__main__":
    # open_example("fileexample.txt")
    write_utf8("fileexample.txt")


