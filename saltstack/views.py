from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from saltstack.models import AppList


def index(request):
    return HttpResponse('Saltstack')


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
    if applist:
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


def init(request):
    if request.method == 'GET':
        return render(request, 'init.html')
    elif request.method == 'POST':
        pass