#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/8/2

import requests
import unittest

class UserTest(unittest.TestCase):
    '''用户查询测试'''
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/users/'
        self.auth=('luwh','1234')

    def test_user1(self):
        r=requests.get(self.base_url+'1/',auth=('luwh','1234'))
        result=r.json()
        self.assertEqual(result['username'],'luwh')
        self.assertEqual(result['email'],'luwh@mail.com')

class EventTest(unittest.TestCase):
    '''发布会测试'''
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/events/'
        self.auth=('luwh','1234')

    def test_event_add(self):
        payload={'name':'小米发布会','limit':2000,'address':'北京',
                 'status':1,'start_time':'2019-11-12 12:30:11'}
        r=requests.post(self.base_url,data=payload,auth=self.auth)
        result=r.json()
        self.assertEqual(result['name'],'小米发布会')


if __name__ == '__main__':
    unittest.main()
