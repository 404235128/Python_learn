#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/5/6

import unittest

def all_case():

    case_dir='D:\\Python-learn\\work\\login_test'

    testcase=unittest.TestSuite()

    discover=unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)

    testcase.addTest(discover)
    print(testcase)
    return testcase

if __name__ == '__main__':
    # runner=unittest.TextTestRunner()
    import HTMLTestRunner
    report_path='D:\\Python-learn\\work\\login_test\\result.html'

    fp=open(report_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='我的测试报告',
        description='测试用例执行结果'
    )
    runner.run(all_case())
    fp.close()
