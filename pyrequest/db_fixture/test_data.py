#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/7/26
import sys
sys.path.append('../db_fixture')
import time
from mysql_db import DB

#创建数据
datas={
    'sign_event':[
        {'id':1,'name':'红米pro发布会','limit':2000,'status':1,'address':'北京会展中心',
         'start_time':'2019-11-12 09:00:00','create_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())},
        {'id':2,'name':'可参加人数为0','limit':0,'status':1,'address':'北京会展中心',
         'start_time':'2019-11-12 09:00:00','create_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())},
        {'id':3,'name':'当前状态为0关闭','limit':2000,'status':0,'address':'北京会展中心',
         'start_time':'2019-11-12 09:00:00','create_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())},
        {'id':4,'name':'发布会已结束','limit':2000,'status':1,'address':'北京会展中心',
         'start_time':'2018-11-12 09:00:00','create_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())},
        {'id':5,'name':'小米发布会','limit':2000,'status':1,'address':'北京国家会议中心',
         'start_time':'2019-11-12 09:00:00','create_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())},
    ],
    'sign_guest':[
        {'id':1,'realname':'alen','phone':13511001100,'email':'alen@mail.com',
         'sign':0,'create_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),'event_id':1},
        {'id': 2, 'realname': 'has in', 'phone': 13511001101, 'email': 'sign@mail.com',
         'sign': 1,'create_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()), 'event_id': 1},
        {'id': 3, 'realname': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com',
         'sign': 0,'create_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()), 'event_id': 5},
    ],
}

#插入数据
def init_data():
    db=DB()
    for table,data in datas.items():
        db.clear(table)
        # print(data)
        for d in data:
            # print(d)
            db.insert(table,d)
    db.close()

if __name__ == '__main__':
    init_data()