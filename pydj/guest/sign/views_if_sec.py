#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: luwh time:2019/7/29

from django.contrib import auth as django_auth
import base64
from django.http import JsonResponse
from sign.models import Event,Guest
from django.core.exceptions import ObjectDoesNotExist
from Crypto.Cipher import AES
import json


#用户认证
def user_auth(request):
    get_http_auth=request.META.get('HTTP_AUTHORIZATION',b'')
    auth=get_http_auth.split()
    try:
        auth_parts=base64.b64decode(auth[1].decode('iso-8859-1').partition(':'))
    except IndexError:
        return 'null'

    userid,password=auth_parts[0],auth_parts[2]
    user=django_auth.authenticate(username=userid,password=password)
    if user is not None and user.is_active:
        django_auth.login(request,user)
        return 'success'
    else:
        return 'fail'

#发布会查询接口--增加用户认证
def get_event_list(request):
    auth_result=user_auth(request)
    if auth_result=='null':
        return JsonResponse({'status':10011,'message':'user auth null'})
    if auth_result=='fail':
        return JsonResponse({'status':10012,'message':'user auth fail'})

    eid=request.GET.get('eid','')
    name=request.GET.get('name','')
    if eid==''and name=='':
        return JsonResponse({'status':10021,'message':'parameter error'})

    if eid!='':
        event={}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022,'message':'query result is empty'})
        else:
            event['name']=result.name
            event['limit']=result.limit
            event['status']=result.status
            event['address']=result.address
            event['start_time']=result.start_time
            return JsonResponse({'status':200,'message':'success','data':event})

    if name!='':
        datas=[]
        results=Event.objects.filter(name__contains=name)
        if results:
            for r in results:
                event={}
                event['name']=r.name
                event['limit']=r.limit
                event['status']=r.status
                event['address']=r.address
                event['start_time']=r.start_time
                datas.append(event)
            return JsonResponse({'status':200,'message':'success','data':datas})
        else:
            return JsonResponse({'status':10022,'message':'query result is empty'})


BS=16
unpad=lambda s:s[0:-ord(s[-1])]

def decryptBase64(src):
    return base64.urlsafe_b64decode(src)

def decryptAES(src,key):
    src=decryptBase64(src)
    iv=b'1172311105789011'
    cryptor=AES.new(key,AES.MODE_CBC,iv)
    text=cryptor.decrypt(src).decode()
    return unpad(text)

def aes_encryption(request):
    app_key=b'W7v4D60fds2Cmk2U'
    if request.method=='POST':
        data=request.POST.get('data','')
    decode=decryptAES(data,app_key)
    dict_data=json.loads(decode)
    return dict_data

def get_guest_list(request):
    dict_data=aes_encryption(request)

    eid=dict_data['eid']
    phone=dict_data['phone']

    if eid=='':
        return JsonResponse({'status':10021,'message':'eid cannot be empty'})
    if eid!='' and phone=='':
        datas=[]
        result=Guest.objects.filter(event_id=eid)
        if result:
            for r in result:
                guest={}
                guest['realname']=r.realname
                guest['phone']=r.phone
                guest['email']=r.email
                guest['sign']=r.sign
                datas.append(guest)
            return JsonResponse({'status':200,'message':'success','data':datas})
        else:
            return JsonResponse({'status':10022,'message':'query result is empty'})

    if eid!='' and phone!='':
        guest={}
        try:
            result=Guest.objects.get(event_id=eid,phone=phone)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022,'message':'query result is empty'})
        else:
            guest['realname']=result.realname
            guest['phone']=result.phone
            guest['email']=result.email
            guest['sign']=result.sign
            return JsonResponse({'status':200,'message':'success','data':guest})