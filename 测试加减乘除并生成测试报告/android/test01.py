#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/5/6

import unittest
import requests

class Test_Android(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login(self):
        a='你好'
        b='HI'
        self.assertEqual(a,b,msg='失败原因：%s不等于%s' % (a,b))

    def testAdd(self):  # test method names begin with 'test'
        u"""测试加法运算1+2=3"""
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)
        print('testAdd')

    def testMultiply(self):
        u"""测试乘法运算"""
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)
        print('testMultiply')

    def testMinus(self):
        self.assertEqual((6-1),5)
        self.assertEqual((25-11),14)
        # print('testMinus')

    def testDivide(self):
        self.assertEqual((7/2),3.5)
        self.assertEqual((15/3),5)
        # print('testDivide')
