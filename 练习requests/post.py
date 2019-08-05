#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/8/2

import requests

#传递data参数
url='http://httpbin.org/post'
payload={'yoyo':'hello world','QQ':'12345678'}
r=requests.post(url,data=payload)
print(r.text)

#传递json参数
import json
data_json=json.dumps(payload)
r=requests.post(url,json=data_json)
print(r.text)