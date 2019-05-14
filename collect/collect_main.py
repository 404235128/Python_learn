#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lwh time:2019/4/1

import os
from operConfig import getconfig,setconfig
from LinkAccessDB import getDcData,getMaxData
from DataRow import DataRow
from LinkSqliteDB import insertdata,dateid
import logging
# import main

def create_logfile():  #生成日志文件
    LOGF_NAME = 'log_' + dateid()+'.txt'
    LOG_PATH = '.\\log\\%s' % LOGF_NAME
    f=open(LOG_PATH,'w')
    f.close()

    INFO_FORMAT = '%(asctime)s:%(levelname)s:%(message)s'
    # WARN_FORMAT = '%(asctime)s:%(levelname)s:%(message)s:%(funcName)s:%(lineno)d'
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(filename=LOG_PATH, level='INFO', \
                        format=INFO_FORMAT,datefmt=DATE_FORMAT)

def collect_main():
    #读取配置文件
    curpath = os.path.abspath('.')
    config_path=os.path.join(curpath,'config.ini')
    dbpath=getconfig(config_path).get('database01')
    processtime=getconfig(config_path).get('processtime01')
    tableid=getconfig(config_path).get('tableid01')


    #根据配置文件连接access数据库,获取新数据
    lists = getDcData(dbpath,processtime,tableid)
    if len(lists)>0:
        i=0
        for i in range(len(lists)):
            rowdata=DataRow(lists[i])
            insertdata(rowdata.time, rowdata.barcode)  #连接sqlite数据库,将获取到的数据插入sqlite数据库
        print('数据更新成功，共%d条新数据' % (len(lists)))
        logging.info('数据更新成功，共%d条新数据' % (len(lists)))
        # main.textBrowser.append('数据更新成功，共%d条新数据' % (len(lists)))
    else:
        print('没有获取到新数据！')
        logging.warning('没有获取到新数据！')
        # main.textBrowser.append('没有获取到新数据！')


    #获取新数据后更新配置文件
    maxdata = getMaxData(dbpath)
    maxdata=tuple(maxdata[0])
    setconfig(config_path,maxdata)




