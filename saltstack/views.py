from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from saltstack.models import AppList


def index(request):
    return HttpResponse('Saltstack')

def installApp(request):
    return render(request, 'installapp.html')

def applist(request):
    resultBean = dict()
    appList = AppList.objects.all()
    if applist:
        try:
            appAll = list()
            for item in appList:
                each = dict()
                each['id'] = item.id
                each['priority'] = item.priority
                each['appname'] = item.appname
                appAll.append(each)
            resultBean['code'] = 200
            resultBean['msg'] = 'success'
            resultBean['data'] = appAll
        except Exception as e:
            resultBean['code'] = 400
            resultBean['msg'] = 'error'
            resultBean['data'] = e
        return JsonResponse(resultBean)
    else:
        resultBean['code'] = 400
        resultBean['msg'] = 'error'
        resultBean['data'] = None

def init(request):
    if request.method == 'GET':
        return render(request, 'init.html')
    elif request.method == 'POST':
        pass