#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/8/9

from selenium import webdriver

browser=webdriver.Chrome()
browser.get('http://localhost:8001')
assert 'Django' in browser.title