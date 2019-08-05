#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/7/30

import time
import hashlib
from django.http import JsonResponse
from sign.models import Event,Guest
from django.core.exceptions import ValidationError

#判断用户签名和时间戳
def user_sign(request):

    client_time=request.POST.get('time','')
    client_sign=request.POST.get('sign','')
    if client_time=='' or client_sign=='':
        return 'sign null'

    #服务器时间
    nowtime=time.time()
    server_time=str(nowtime).split('.')[0]
    #时间差
    time_diff=int(server_time)-int(client_time)
    if time_diff>=60:
        return 'timeout'

    #签名检查
    md5=hashlib.md5()
    sign_str=client_time+'&Guest-Bugmaster'
    sign_bytes_utf8=sign_str.encode(encoding='utf-8')
    md5.update(sign_bytes_utf8)
    sever_sign=md5.hexdigest()
    if sever_sign!=client_sign:
        return 'sign error'
    else:
        return 'sign right'

#添加发布会接口
def add_event(request):
    sign_result=user_sign(request)
    if sign_result=='sign null':
        return JsonResponse({'status':10011,'message':'user sign null'})
    elif sign_result=='timeout':
        return JsonResponse({'status':10012,'message':'user sign timeout'})
    elif sign_result=='sign error':
        return JsonResponse({'status':10013,'message':'user sign error'})

    eid=request.POST.get('eid','')
    name=request.POST.get('name','')
    limit=request.POST.get('limit','')
    status=request.POST.get('status','')
    address=request.POST.get('address','')
    start_time=request.POST.get('start_time','')

    if eid=='' or name=='' or limit=='' or address=='' or start_time=='':
        return JsonResponse({'status':10021,'message':'parameter error'})

    result=Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status':10022,'message':'event id already exists'})

    result=Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status':10023,'message':'event name already exists'})

    if status=='':
        status=1

    try:
        Event.objects.create(id=eid,name=name,limit=limit,address=address,status=int(status),start_time=start_time)
    except ValidationError as e:
        error='start_time format error.It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status':10024,'message':error})

    return JsonResponse({'status':200,'message':'add event success'})