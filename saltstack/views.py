import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from saltstack.models import AppList, IpList
from util.saltapi import SaltServer


def result(code, msg, data):
    resultBean = dict()
    resultBean['code'] = code
    resultBean['msg'] = msg
    resultBean['data'] = data
    return resultBean


def applist(request):
    appList = AppList.objects.all()
    if appList:
        appAll = list()
        for item in appList:
            each = dict()
            each['id'] = item.id
            each['priority'] = item.priority
            each['appname'] = item.appname
            appAll.append(each)
        return JsonResponse(result(200, 'success', appAll))
    else:
        return JsonResponse(result(400, 'error', None))



# def iplist(request):
#     IPList = IpList.objects.all()
#     ipAll = list()
#     for item in IPList:
#         each = dict()
#         each['id'] = item.id
#         each['ipnum'] = item.ipnum
#         ipAll.append(each)
#     return JsonResponse(result(200, 'success', ipAll))


@login_required
def init(request):
    if request.method == 'GET':
        return render(request, 'init.html')
    elif request.method == 'POST':
        saltServer = SaltServer()
        iptext = request.POST.get('iptext', None) #获取字符形式的值
        checkbox = request.POST.getlist('Checkbox', None)  #获取列表的值
        initDict = {    #添加一个dict用于维护
            '1': 'publicKey',
            '2': 'installMinion',
            # '3': 'syncTime',
            # '4': 'deployYum',
            # '5': 'installSNMP',
            # '6': 'deployDNS',
        }
        resList = list()
        if len(checkbox) > 0:
            for i in checkbox:
                if i in initDict.keys():
                    for ip in iptext.split(','):
                        if ip.strip():
                            iplist = IpList.objects.all().values('ipnum')
                            print(ip.strip())
                            print(iplist)
                            print('#' * 50)
                            #判断输入的ip是否存在于数据库中，没有则添加进去
                            if {'ipnum': ip.strip()} in iplist:
                                print('the ip:{0} is already existed in db'.format(ip.strip()))
                                print('*' * 50)
                            else:
                                IpList.objects.create(ipnum=ip.strip())
                                print('the ip:{0} is save to db'.format(ip.strip()))
                                print('@' * 50)
                            res = saltServer.runRunner('masterApp.' + initDict.get(i), ip=ip.strip())
                            resList.append(res)
        return JsonResponse(result(200, 'success', resList))


@login_required
def installApp(request):
    app_list = AppList.objects.all()
    ip_list = IpList.objects.all().values('ipnum')  #只取ipnum这一列数据
    return render(request, 'installapp.html', {'app_list': app_list, 'ip_list': ip_list})


def ip(request):
    ip_list = IpList.objects.all().values('ipnum')
    return render(request, 'ip.html', {'ip_list': ip_list})  #直接将函数中的所有变量全部传给模板,以字典的类型，等价于locals()


def dailyCheck(request):
    if request.method == 'GET':
        return render(request, 'dailycheck.html')
    elif request.method == 'POST':
        saltServer = SaltServer()
        bt1 = request.POST.get('server', None)
        bt2 = request.POST.get('db', None)
        if bt1:
            data = saltServer.runRunner('dailycheck.checkserver')
            return render(request, 'dailycheck.html', {'data': data.get('data')[0]})
        elif bt2:
            data = saltServer.runRunner('dailycheck.checkdb')
            return render(request, 'dailycheck.html', {'data': data.get('data')[0]})

