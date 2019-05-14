#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lwh time:2019/3/29

import configparser

#获取配置文件内容，并存放到字典
def getconfig(path):
    cf = configparser.ConfigParser()
    cf.read(path, encoding='GB2312')
    database01 = cf.get('MulSourceDB', 'Database01')
    processtime01 = cf.get('MulSourceDB', 'ProcessTime01')
    tableid01 = cf.get('MulSourceDB', 'TableId01')
    dicts={'processtime01':processtime01,'database01':database01,'tableid01': tableid01}
    return dicts

#更新配置文件
def setconfig(path,*conf):
    cf = configparser.ConfigParser()
    cf.read(path, encoding='GB2312')
    cf.set('MulSourceDB', 'ProcessTime01', str(conf[0][0]))
    cf.set('MulSourceDB', 'TableId01', str(conf[0][1]))
    cf.write(open(path, 'w'))
