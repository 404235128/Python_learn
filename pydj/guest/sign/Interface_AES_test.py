#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/7/31

from Crypto.Cipher import AES
import base64
import requests
import unittest
import json

class AESTest(unittest.TestCase):

    def setUp(self):
        BS=16
        #对接口参数进行补足长度16
        self.pad=lambda s:s+(BS-len(s) % BS)* chr(BS-len(s) % BS)

        self.base_url='http://127.0.0.1:8000/api/sec_get_guest_list/'
        self.app_key=b'W7v4D60fds2Cmk2U'

    def encryptBase64(self,src):
        s1=base64.urlsafe_b64encode(src)
        return s1

    def encryptAES(self,src,key):
        iv=b'1172311105789011'
        cryptor=AES.new(key,AES.MODE_CBC,iv)
        s=self.pad(src)
        ciphertext=cryptor.encrypt(s.encode(encoding='utf-8'))
        return self.encryptBase64(ciphertext)

    def test_aes_interface(self):
        payload={'eid':'1','phone':'13511001100'}
        payload_json=json.dumps(payload)
        encoded=self.encryptAES(payload_json,self.app_key).decode()
        r=requests.post(self.base_url,data={'data':encoded})
        result=r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'success')