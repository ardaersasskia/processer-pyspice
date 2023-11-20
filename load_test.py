'''
Author: Ardaer yuanxiaowei135@163.com
Date: 2023-11-19 00:46:22
LastEditors: Ardaer yuanxiaowei135@163.com
LastEditTime: 2023-11-20 13:06:58
FilePath: \processer-pyspice\load_test.py
Description: testbench for cpu load, 2 processes now

Copyright (c) 2023 by Ardaer, All Rights Reserved. 
'''

from multiprocessing import Process
import math, time
from func_timeout import func_set_timeout,exceptions
@func_set_timeout(5)
def load():
    tmp=7.0
    while True:
        tmp=tmp**math.e
        if tmp >= 1.7976931348623157e+100:
                tmp=7
def task():
    tmp=7.0
    while True:
        try:
            load()
        except exceptions.FunctionTimedOut:
            time.sleep(5)
if __name__=='__main__':
    p1=Process(target=task)
    p2=Process(target=task)
    p1.start()
    p2.start()