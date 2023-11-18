'''
Author: Ardaer yuanxiaowei135@163.com
Date: 2023-11-19 00:46:22
LastEditors: Ardaer yuanxiaowei135@163.com
LastEditTime: 2023-11-19 01:02:13
FilePath: \processer-pyspice\load_test.py
Description: testbench for cpu load, 2 processes now

Copyright (c) 2023 by Ardaer, All Rights Reserved. 
'''

from multiprocessing import Processes
import math

def task():
    tmp=7.0
    while True:
        tmp=tmp**math.e
        if tmp >= 100000:
            tmp=7
if __name__=='__main__':
    p1=Process(target=task)
    p2=Process(target=task)
    p1.start()
    p2.start()