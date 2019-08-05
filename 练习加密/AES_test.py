#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/7/31

from Crypto.Cipher import AES

#加密
obj=AES.new(b'This is a key123',AES.MODE_CBC,b'This is an IV456')#生成密钥
message=b'The answer is no'
ciphertext=obj.encrypt(message)#用密钥加密
print(ciphertext)

#解密
obj2=AES.new(b'This is a key123',AES.MODE_CBC,b'This is an IV456')#生成密钥
s=obj2.decrypt(ciphertext)#用密钥解密
print(s)