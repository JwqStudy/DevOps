from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from saltstack.models import AppList, IpList
from util.saltapi import SaltServer


def index(request):
    return render(request, 'init.html')


def installApp(request):
    return render(request, 'installapp.html')


def result(code, msg, data):
    resultBean = dict()
    resultBean['code'] = code
    resultBean['msg'] = msg
    resultBean['data'] = data
    return resultBean


def applist(request):
    appList = AppList.objects.all()
    if appList:
        try:
            appAll = list()
            for item in appList:
                each = dict()
                each['id'] = item.id
                each['priority'] = item.priority
                each['appname'] = item.appname
                appAll.append(each)
            return JsonResponse(result(200, 'success', appAll))
        except Exception as e:
            return JsonResponse(result(400, 'error', e))
    else:
        return JsonResponse(result(400, 'error', None))


def iplist(request):
    IPList = IpList.objects.all()
    ipAll = list()
    for item in IPList:
        each = dict()
        each['id'] = item.id
        each['ipnum'] = item.ipnum
        ipAll.append(each)
    return JsonResponse(result(200, 'success', ipAll))


@login_required
def init(request):
    if request.method == 'GET':
        return render(request, 'init.html')
    elif request.method == 'POST':
        saltServer = SaltServer()
        iptext = request.POST.get('iptext', None) #获取字符形式的值
        checkbox = request.POST.getlist('Checkbox', None)  #获取列表的值
        initDict = {
            '1': 'publicKey',
            '2': 'installMinion',
        }
        resList = list()
        if len(checkbox) > 0:
            for i in checkbox:
                if i in initDict.keys():
                    for ip in iptext.split(','):
                        if ip.strip():
                            res = saltServer.runRunner('masterApp.' + initDict.get(i), ip=ip.strip())
                            resList.append(res)
        return JsonResponse(result(200, 'success', resList))


def ip(request):
    ip_list = IpList.objects.all().values('ipnum')  #只取ipnum这一列数据
    return render(request, 'ip.html', {'ip_list': ip_list})  #直接将函数中的所有变量全部传给模板,以字典的类型，等价于locals()


def api(request):
    ip1 = IpList(ipnum='192.168.137.140')
    ip1.save()
    print('{0} save successful'.format(ip1))
    return HttpResponse('save successful')