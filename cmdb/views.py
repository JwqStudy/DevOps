from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from cmdb.models import Host, HostGroup
import pickle
import json


def cmdbIndex(request):
    assets = Host.objects.all()
    return render(request, 'summary.html', locals())


def autocollect(request):   #通过脚本传入此api记录参数
    if request.POST:
        # obj = pickle.loads(request.body)   #把客户端传输过来的在内存中的数据通过pickle进行反序列化解析，是一个字典形式
        obj = json.loads(request.body)   #把客户端传输过来的在内存中的数据通过json进行反序列化解析，是一个字典形式
        print(obj)
        hostname = obj['hostname']    #这个是通过序列化的方式取值，区别于下面的的通过post方法取值，但是结果都是一样
        ip = obj['ip']
        osver = obj['osver']
        vendor = obj['vendor']
        product = obj['product']
        sn = obj['sn']
        cpu_model = obj['cpu_model']
        cpu_num = obj['cpu_num']
        memory = obj['memory']
        # hostname = request.POST.get('hostname')
        # ip = request.POST.get('ip')
        # osver = request.POST.get('osver')
        # vendor = request.POST.get('vendor')
        # product = request.POST.get('product')
        # sn = request.POST.get('sn')
        # cpu_model = request.POST.get('cpu_model')
        # cpu_num = request.POST.get('cpu_num')
        # memory = request.POST.get('memory')
        '''这里从数据库中查找sn的值用作判断和上面获取到的sn是否相等，查到了会返回那个对象，
        接着执行下面操作重写相关纪录，如果查不到返回异常就要重新创建一条纪录'''
        try:
            host = Host.objects.get(sn=sn)
        except:
            host = Host()   #这样可以重新创建一条新纪录

        host.hostname = hostname
        host.ip = ip
        host.osver = osver
        host.vendor = vendor
        host.product = product
        host.sn = sn
        host.cpu_model = cpu_model
        host.cpu_num = cpu_num
        host.memory = memory
        host.save()
        return HttpResponse('OK')
    else:
        return render(request, 'manualcollect.html')


def manualcollect(request):
    if request.method == 'GET':
        return render(request, 'manualcollect.html')
    elif request.method == 'POST':
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        osver = request.POST.get('osver')
        vendor = request.POST.get('vendor')
        product = request.POST.get('product')
        sn = request.POST.get('sn')
        cpu_model = request.POST.get('cpu_model')
        cpu_num = request.POST.get('cpu_num')
        memory = request.POST.get('memory')
        if hostname == '' or ip == '' or osver == '' or vendor == '' or product == '' or sn == '' or cpu_model == '' or cpu_num == '' or memory == '':
            return render(request, 'manualcollect.html', locals())
        else:
            try:
                host = Host.objects.get(sn = sn)
            except:
                host = Host()
            host.hostname = hostname
            host.ip = ip
            host.osver = osver
            host.vendor = vendor
            host.product = product
            host.sn = sn
            host.cpu_model = cpu_model
            host.cpu_num = cpu_num
            host.memory = memory
            host.save()
            return render(request, 'manualcollect.html')


"""从数据库取出组的数据输出json格式的api"""
def getjson(request):
    ret_list = list()
    hg = HostGroup.objects.all()
    for g in hg:
        ret = {'groupname': g.groupname, 'members': []}
        for h in g.members.all():
            ret_h = {'hostname': h.hostname, 'ip': h.ip}
            ret['members'].append(ret_h)
        ret_list.append(ret)
    return HttpResponse(json.dumps(ret_list))


"""从数据库取出组的数据输出txt格式的api"""
def gettxt(request):
    result = ''
    hg = HostGroup.objects.all()
    for g in hg:
        groupname = g.groupname
        for h in g.members.all():
            hostname = h.hostname
            ip = h.ip
            result += groupname+' '+hostname+' '+ip+'\n'
    return HttpResponse(result)