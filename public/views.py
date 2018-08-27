import yagmail as yagmail
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def cms_login(request):
    error_msg = ''
    if request.method == 'GET':
        return render(request, 'login.html', {'error': error_msg})
    else:
        print(request.POST, '-' * 10)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        remember = request.POST.get('remember', None)
        print(username)
        print(password)
        print(remember)

        # 1. 先用authenticate进行验证
        user = authenticate(username=username, password=password)
        if user:
            # 2. 需要登录,
            # 3. 我们的login视图函数不要和login重名
            login(request, user)
            print('login success')
            # 判断如果有remember,那么说明需要记住,使用None将
            # 使用settings.py中SESSION_COOKIE_AGE指定的值,
            # 这个值默认是14天
            if remember:
                request.session.set_expiry(None)
            else:
                # 浏览器一旦关闭,session就会过期
                request.session.set_expiry(0)
            nexturl = request.GET.get('next')
            print('###'*10)
            print(nexturl)
            print('###'*10)
            if nexturl:
                return redirect(nexturl)
            else:
                return redirect(reverse('devindex'))
        else:
            error_msg = '用户名或密码错误'
            return render(request, 'login.html', {'error': error_msg})


def cms_signup(request):
    return render(request, 'signup.html')


def cms_logout(request):
    logout(request)
    return redirect(reverse('cms_login'))


def index(request):
    return render(request, 'base.html')


def opsIndex(request):
    return render(request, 'index.html')


def publicIndex(request):
    return render(request, 'public.html')
    # return HttpResponseNotFound('<h1>not found</h1>')


def setting(request):
    if request.method == 'GET':
        return render(request, 'setting.html')
    elif request.method == 'POST':
        newEmail = request.POST.get("newEmail")
        print(newEmail)
        sendUrl = request.scheme + '://' + request.get_host() + "/public/check/email/" + newEmail
        print(sendUrl)
        subject = "Update email address"
        message = "邮箱更改地址，请点击 " + sendUrl + " 请在5分钟之内完成注册，否则过期无效\n" + "工作人员不会向您索取链接，请谨慎操作！"
        yag = yagmail.SMTP(user='15692421430@163.com', password='15692421430com',host='smtp.163.com', port=465)
        yag.send(to=newEmail, subject=subject, contents=message)
        resultBean = dict()
        resultBean['code'] = 200
        resultBean['msg'] = 'success'
        resultBean['data'] = None
        return JsonResponse(resultBean)
    else:
        return HttpResponse("请求方法不符合只接受get和post!")


def checkEmail(request, email):
    try:
        user = request.user
        user.email = email
        user.save(update_fields=['email'])
        return HttpResponse("邮箱修改成功!")
    except Exception as e:
        return HttpResponse("该链接已经生效")