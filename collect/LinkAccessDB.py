#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lwh time:2019/3/29

from operConfig import getconfig
import pypyodbc

'''获取access数据库中的新数据
dbpath：数据库存放路径
processtime：查询条件
tableid：查询条件
'''
def getDcData(dbpath,processtime,tableid):
    sql='select 数据绑定号 as barcode,测量时间 as testdate,测量类型 as testType, 是否合格 as quality_type from 测量数据表1 where 测量时间>=#%s# and ID>%s' % (processtime,tableid)
    conn = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=%s' % dbpath
    db=pypyodbc.win_connect_mdb(conn)                 # 打开数据库连接
    cur= db.cursor()
    cur.execute(sql)
    # cur.execute('select 数据绑定号 as barcode,测量时间 as testdate,测量类型 as testType,  \
    # 是否合格 as quality_type from 测量数据表1 where 测量时间>=? and ID>?',(processtime,tableid))
    values=cur.fetchall()
    cur.close()
    db.commit()
    db.close()
    return values

def getMaxData(dbpath):
    sql='select top 1 测量时间 as testdate,ID from 测量数据表1 order by ID desc'
    conn='Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=%s' % dbpath
    db=pypyodbc.win_connect_mdb(conn)
    cur=db.cursor()
    cur.execute(sql)
    values=cur.fetchall()
    cur.close()
    db.commit()
    db.close()
    return values
