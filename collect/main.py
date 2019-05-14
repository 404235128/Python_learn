#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lwh time:2019/3/26

import sys
from main_frm import Ui_MainWindow
# from collect_main import collect_main,create_logfile
import collect_main
import time
import threading
import logging
from PyQt5.QtWidgets import QApplication,QMainWindow

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)

    collect_main.create_logfile()
    flag=0
    def stop_click(self):
        global flag
        flag = 0
        # print(flag)
        logging.info('采集停止')
        self.textBrowser.append('采集停止')

    def exec_collect(self):       #执行采集函数
        global flag
        # print(flag)
        while True:
            if flag==1:
                collect_main.collect_main()
                time.sleep(15)
            else:
                break

    def run_click(self):
        global flag
        flag=1
        # print(flag)
        logging.info('开始采集')
        self.textBrowser.append('开始采集')
        t = threading.Thread(target=self.exec_collect, args='')      #创建采集线程
        t.setDaemon(True)        #以守护的方式运行
        t.start()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ui=Main()
    ui.show()
    sys.exit(app.exec_())