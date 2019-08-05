#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/7/31

from Crypto.Hash import SHA256

hash=SHA256.new()
hash.update(b'message')
#h=hash.digest()
h=hash.hexdigest()
print(h)