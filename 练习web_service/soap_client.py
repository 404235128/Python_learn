#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/8/1
from suds.client import Client
from suds.xsd.doctor import ImportDoctor,Import

#查询手机号码归属地
# url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
# client=Client(url)
# result=client.service.getMobileCodeInfo(13738090510)
# print(result)

#查询天气预报
url1='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl'
imp=Import('http://www.w3.org/2001/XMLSchema',location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://WebXml.com.cn/')
client1=Client(url1,plugins=[ImportDoctor(imp)])
result1=client1.service.getWeather('杭州')
print(result1)