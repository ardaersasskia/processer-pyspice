'''
Author: Ardaer yuanxiaowei135@163.com
Date: 2023-11-19 00:46:22
LastEditors: Ardaer yuanxiaowei135@163.com
LastEditTime: 2023-11-19 01:07:34
FilePath: \processer-pyspice\load_test.py
Description: testbench for cpu load, 4 processes now

Copyright (c) 2023 by Ardaer, All Rights Reserved. 
'''

from multiprocessing import Process
import math

def task():
    tmp=7.0
    while True:
        tmp=tmp**math.e
        if tmp >= 1.7976931348623157e+100:
            tmp=7
if __name__=='__main__':
    p1=Process(target=task)
    p2=Process(target=task)
    p3=Process(target=task)
    p4=Process(target=task)
    p1.start()
    p2.start()
    p3.start()
    p4.start()