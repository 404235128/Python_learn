#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lwh time:2019/4/1

import sqlite3
import re
from datetime import datetime

#将当前时间转化为dataid返回
def dateid():
    date = str(datetime.now())      #获取系统当前时间并转化为str类型
    datelist=re.split(r'[\-\s\:\.]+',date)    #将时间中的分割符-，：以及空格去掉
    datestr=''.join(datelist)        #拼接成字符串
    return datestr

#插入数据到sqlite数据库
def insertdata(picktime,bar_code):
    sql='insert into dc_data(data_id,infectant_id,pick_time,context) values (\'%s\',-1,\'%s\',\'%s\')' % (dateid(), picktime,bar_code)
    conn = sqlite3.connect('prodb_20190329.db')
    cur = conn.cursor()
    # print(sql)
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

