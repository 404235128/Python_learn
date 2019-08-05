#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/8/2

import requests

#get请求
url='http://www.baidu.com'
r=requests.get(url)
print(r.status_code)
print(r.text)
print(r.encoding)
print(r.content)
print(r.headers)
print(r.cookies)

#带参数的get请求
url='http://zzk.cnblogs.com/s/blogpost'
par={'Keywords':'yoyoketang'}
r=requests.get(url,params=par)
print(r.status_code)
print(r.text)