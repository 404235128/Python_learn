#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/7/30

import unittest
import requests

class GetEventListTest(unittest.TestCase):
    '''查询发布会接口测试'''
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/api/sec_get_event_list/'
        self.auth_user=('luwh','1234')

    def test_get_event_list_auth_null(self):
        '''user为null'''
        r=requests.get(self.base_url,params={'eid':''})
        result=r.json()
        self.assertEqual(result['status'],10011)
        self.assertEqual(result['message'],'user auth null')

    def test_get_event_list_auth_error(self):
        '''user错误'''
        r=requests.get(self.base_url,auth=('luwh','123'),params={'eid':''})
        result=r.json()
        self.assertEqual(result['status'],10012)
        self.assertEqual(result['message'],'user auth fail')

    def test_get_event_list_eid_and_name_null(self):
        '''eid和name为空'''
        r=requests.get(self.base_url,auth=self.auth_user,params={'eid':'','name':''})
        result=r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'parameter error')

    def test_get_event_list_eid_error(self):
        '''根据eid查询结果为空'''
        r=requests.get(self.base_url,auth=self.auth_user,params={'eid':'14'})
        result=r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],'query result is empty')

    def test_get_event_list_name_error(self):
        '''根据name查询结果为空'''
        r=requests.get(self.base_url,auth=self.auth_user,params={'eid':'1','name':'小米发布会'})
        result=r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'], 'query result is empty')

    def test_get_event_list_eid_success(self):
        '''根据eid查询成功'''
        r=requests.get(self.base_url,auth=self.auth_user,params={'eid':'1'})
        result=r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'success')
        self.assertEqual(result['data']['name'],'红米pro发布会')
        self.assertEqual(result['data']['address'],'北京会展中心')

    def test_get_event_list_name_success(self):
        '''根据name查询成功'''
        r=requests.get(self.base_url,auth=self.auth_user,params={'eid':'1','name':'红米pro发布会'})
        result=r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'success')
        self.assertEqual(result['data']['address'],'北京会展中心')