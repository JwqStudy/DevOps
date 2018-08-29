from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from cmdb.models import Host


def cmdbIndex(request):
    return render(request, 'cmdb.html')


def collect(request):
    if request.POST:
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        osver = request.POST.get('osver')
        vendor = request.POST.get('vendor')
        product = request.POST.get('product')
        sn = request.POST.get('sn')
        cpu_model = request.POST.get('cpu_model')
        cpu_num = request.POST.get('cpu_num')
        memory = request.POST.get('memory')

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
        return HttpResponse('OK')
    else:
        return HttpResponse('not data')