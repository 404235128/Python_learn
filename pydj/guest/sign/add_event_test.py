#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/7/30

import unittest
import time
import hashlib
import requests

class AddEventTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/api/sec_add_event/'
        self.api_key='&Guest-Bugmaster'

        now_time=time.time()
        self.client_time=str(now_time).split('.')[0]

        md5=hashlib.md5()
        sign_str=self.client_time+self.api_key
        sign_bytes_utf8=sign_str.encode(encoding='utf-8')
        md5.update(sign_bytes_utf8)
        self.sign_md5=md5.hexdigest()

    def test_add_event_sign_null(self):
        '''签名信息为空'''
        payload={'eid':1,'name':'','limit':'','address':'','start_time':'',
                 'time':'','sign':''}
        r=requests.post(self.base_url,data=payload)
        result=r.json()
        self.assertEqual(result['status'],10011)
        self.assertEqual(result['message'],'user sign null')

    def test_add_event_sign_timeout(self):
        '''添加发布会超时'''
        now_time=str(int(self.client_time)-61)
        payload={'eid':1,'name':'','limit':'','address':'','start_time':'',
                 'time':now_time,'sign':'abc'}
        r=requests.post(self.base_url,data=payload)
        result=r.json()
        self.assertEqual(result['status'],10012)
        self.assertEqual(result['message'],'user sign timeout')

    def test_add_event_sign_error(self):
        '''签名信息错误'''
        payload={'eid':1,'name':'','limit':'','address':'','start_time':'',
                 'time':self.client_time,'sign':'abc'}
        r=requests.post(self.base_url,data=payload)
        result=r.json()
        self.assertEqual(result['status'],10013)
        self.assertEqual(result['message'],'user sign error')

    def test_add_event_eid_null(self):
        '''eid为空'''
        payload={'eid':'','name':'','limit':'','address':'','start_time':'',
                 'time':self.client_time,'sign':self.sign_md5}
        r=requests.post(self.base_url,data=payload)
        result=r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'parameter error')

    def test_add_event_eid_exist(self):
        '''eid已存在'''
        payload={'eid':'1','name':'粉米发布会','limit':'2000','address':'天津','start_time':'2019-11-17 08:56:18',
                 'time':self.client_time,'sign':self.sign_md5}
        r=requests.post(self.base_url,data=payload)
        result=r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],'event id already exists')

    def test_add_event_name_exist(self):
        '''发布会name已存在'''
        payload={'eid':'13','name':'小米发布会','limit':'2000','address':'北京','start_time':'2019-11-17 08:56:18',
                 'time':self.client_time,'sign':self.sign_md5}
        r=requests.post(self.base_url,data=payload)
        result=r.json()
        self.assertEqual(result['status'],10023)
        self.assertEqual(result['message'],'event name already exists')

    def test_add_event_date_type_error(self):
        '''日期格式错误'''
        payload = {'eid': '13', 'name': '粉米发布会', 'limit': '2000', 'address': '天津', 'start_time': '2019',
                   'time': self.client_time, 'sign': self.sign_md5}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10024)
        self.assertIn('start_time format error',result['message'])

    def test_add_event_success(self):
        '''添加发布会成功'''
        payload = {'eid': '13', 'name': '粉米发布会', 'limit': '2000', 'address': '天津', 'start_time': '2019-11-17 08:56:18',
                   'time': self.client_time, 'sign': self.sign_md5}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'],'add event success')
