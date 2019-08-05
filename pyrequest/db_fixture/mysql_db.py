#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/7/26

import pymysql.cursors
import os
import configparser as cparser

# base_dir=str(os.path.dirname(os.path.dirname(__file__)))
# base_dir=base_dir.replace('\\','/')
# conf_path=base_dir+'/db_config.ini'
#获取配置文件路径
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf_path=os.path.join(base_dir,'db_config.ini')
# print(conf_path)
#读取配置文件内容
cf=cparser.ConfigParser()
cf.read(conf_path,encoding='GB2312')

host=cf.get('mysqlconf','host')
port=cf.get('mysqlconf','port')
user=cf.get('mysqlconf','user')
password=cf.get('mysqlconf','password')
db=cf.get('mysqlconf','db_name')

#数据库操作
class DB:

    def __init__(self):
        try:
            #连接数据库
            self.connection=pymysql.connect(
                host=host,
                user=user,
                password=password,
                db=db,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.err.OperationalError as e:
            print('Mysql Error %d:%s' % (e.args[0],e.args[1]))

    #清除表数据
    def clear(self,table_name):
        real_sql='delete from '+table_name+';'
        with self.connection.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
            cursor.execute(real_sql)
        self.connection.commit()

    #插入数据
    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key]="'"+str(table_data[key])+"'"

        key_list=[]
        for k in table_data.keys():
            k="`"+str(k)+"`"
            key_list.append(k)
        key_str=','.join(key_list)
        value=','.join(table_data.values())
        real_sql="insert into "+table_name+" (" + key_str + ") values (" + value + ");"
        # print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    #关闭连接数据库
    def close(self):
        self.connection.close()


    if __name__ == '__main__':
        db=DB()
        table_name='sign_event'
        data={'id':1,'name':'红米','limit':2000,'status':1,'address':'北京会展中心',
              'start_time':'2019-11-12 08:30:00'}
        table_name2='sign_guest'
        data2={'realname':'alen','phone':13711001100,'email':'alen@mail.com','sign':0,
               'event_id':1}

        db.clear(table_name)
        db.insert(table_name,data)
        db.close()