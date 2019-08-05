from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def index(request):
    # return HttpResponse('Hello Django!')
    return render(request,'index.html')

#登录动作
def login_action(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password) #用户名密码都正确时返回user，否则返回None
        if user is not None:
            auth.login(request,user) #登录
            request.session['user'] = username  # 将session信息记录到浏览器
            response= HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',username,3600)  #添加浏览器cookie
            return response
        else:
            return render(request,'index.html',{'error':'用户名或密码错误！'})
    else:
        return render(request,'index.html',{'error':'用户名或密码错误！'})

#发布会管理
#@login_required
def event_manage(request):
    event_list=Event.objects.all()
    #username=request.COOKIES.get('user','') #读取浏览器cookie
    username=request.session.get('user','') #读取浏览器session
    return render(request,"event_manage.html",{'user':username,'events':event_list})

#发布会名称搜索
#@login_required
def search_name(request):
    username=request.session.get('user','')
    search_name=request.GET.get('name','')
    event_list=Event.objects.filter(name__contains=search_name)
    return render(request,'event_manage.html',{'user':username,'events':event_list})

#嘉宾管理
#@login_required
def guest_manage(request):
    username=request.session.get('user','')
    guest_list=Guest.objects.all()
    pages=Paginator(guest_list,2)
    page=request.GET.get('page')          #通过GET请求得到当前要显示第几页的数据
    try:
        contacts=pages.page(page)
    except PageNotAnInteger:
        contacts=pages.page(1)
    except EmptyPage:
        contacts=pages.page(pages.num_pages)
    return render(request,'guest_manage.html',{'user':username,'guests':contacts})

#嘉宾手机号搜索
# @login_required
def search_phone(request):
    username = request.session.get('user', '')
    search_phone=request.GET.get('phone','')
    guest_list=Guest.objects.filter(phone__contains=search_phone)
    pages=Paginator(guest_list,2)
    page=request.GET.get('page')
    try:
        contacts=pages.page(page)
    except PageNotAnInteger:
        contacts=pages.page(1)
    except EmptyPage:
        contacts=pages.page(pages.num_pages)
    return render(request,'guest_manage.html',{'user':username,'guests':contacts,'phone':search_phone})

#签到页面
@login_required
def sign_index(request,event_id):
    event=get_object_or_404(Event,id=event_id)
    guestall=Guest.objects.filter(event_id=event_id)
    guestnum=len(guestall)
    guestsign=Guest.objects.filter(event_id=event_id,sign='1')
    guestsignnum=len(guestsign)
    return render(request,'sign_index.html',{'event':event,'guestnum':guestnum,'guestsignnum':guestsignnum})


#签到动作
# @login_required
def sign_index_action(request,event_id):
    event=get_object_or_404(Event,id=event_id)
    phone=request.POST.get('phone','')
    #获取当前发布会的嘉宾总数和已签到嘉宾数
    guestall = Guest.objects.filter(event_id=event_id)
    guestnum = len(guestall)
    guestsign = Guest.objects.filter(event_id=event_id, sign='1')
    guestsignnum = len(guestsign)

    result=Guest.objects.filter(phone=phone)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'phone error.','guestnum':guestnum,'guestsignnum':guestsignnum})
    result=Guest.objects.filter(phone=phone,event_id=event_id)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'event id or phone error.','guestnum':guestnum,'guestsignnum':guestsignnum})
    result=Guest.objects.get(phone=phone,event_id=event_id)
    if result.sign:
        return render(request,'sign_index.html',{'event':event,'hint':'user has sign in.','guestnum':guestnum,'guestsignnum':guestsignnum})
    else:
        Guest.objects.filter(phone=phone,event_id=event_id).update(sign='1')
        #签到后获取最新的已签到嘉宾数
        guestsign = Guest.objects.filter(event_id=event_id, sign='1')
        guestsignnum = len(guestsign)
        return render(request,'sign_index.html',{'event':event,'hint':'sign in success!','guest':result,'guestnum':guestnum,'guestsignnum':guestsignnum})

#退出系统
@login_required
def logout(request):
    auth.logout(request)
    response=HttpResponseRedirect('/index/')
    return response