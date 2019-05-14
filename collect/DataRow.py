#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lwh time:2019/4/1

#创建类用于实例化记录对象
class DataRow:
    def __init__(self,*n):
        self.barcode=n[0][0]
        self.time=n[0][1]
        self.type=n[0][2]
        self.quality_type=n[0][3]

