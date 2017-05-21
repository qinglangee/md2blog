# -*- coding: utf-8 -*-
import logging


# 设置日志配置
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %Y-%m-%d %H:%M:%S',
                filename='myapp.log',
                filemode='a')
                
                
def debug(content):
    print content
def info(content):
    print content
def warn(content):
    print content
def error(content):
    print content