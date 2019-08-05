#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/7/26

import time,sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
import HTMLTestRunner
import unittest
from db_fixture import test_data

test_dir='./interface'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='*test.py')

if __name__ == '__main__':
    test_data.init_data()
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    report_path='./report/'+now+'_result.html'
    fp=open(report_path,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试报告标题',
        description='测试用例执行结果'
    )
    runner.run(discover)
    fp.close()
