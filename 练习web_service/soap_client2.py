#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/8/1

from suds.client import Client

url='http://127.0.0.1:8000/?wsdl'
client=Client(url)
result=client.service.say_hello('luwh',2)
print(result)