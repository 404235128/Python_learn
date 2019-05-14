#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lwh time:2019/3/29

import  win32com.client
conn=win32com.client.gencache.EnsureDispatch('ADODB.Connection')
conn.ConnectionString ='Provider=Microsoft.ACE.OLEDB.12.0;Data Source=D:/Python-learn/work/test01/INSPC.mdb;'
conn.Open()