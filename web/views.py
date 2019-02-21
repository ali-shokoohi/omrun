from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees, Comments
from hashlib import md5

def logging(username, password):
    try:
        user_check = Employees.objects.filter(personnelـid=username).exists()
        if user_check is True:
            user = Employees.objects.filter(personnelـid=username).get()
            pass_hash = md5(password.encode("utf-8")).hexdigest()
            if user.password == pass_hash:
                return True
            else:
                return False
        else:
            return False
    except:
        return False

def index(request):
    employees = Employees.objects.all()
    comments = Comments.objects.all()
    context = {
        "employees": employees,
        "comments": comments,
        }
    return render(request=request, template_name="index/index.html", context=context)

def login(request):
    if request.session.has_key('user_id'):
        return HttpResponse(content="You logged at last!")
    else:
       if request.method == 'POST':
            if ("username" in request.POST) and ("password" in request.POST):
                username = request.POST['username']
                password = request.POST['password']
                if logging(username, password) is True:
                    request.session['user_id'] = username
                    return HttpResponse(content="You logged successfully!")
                else:
                    error = "!نام کاربری یا کلمه عبود اشتباه میباشد"
                    context = {
                        "error": error,
                    }
                    return render(request=request, template_name="login/login.html", context=context)
            else:
                error = "!لطفا همه فیلد ها را پر کنید"
                context = {
                    "error": error,
                }
                return render(request=request, template_name="login/login.html", context=context)
       else:
           return render(request=request, template_name="login/login.html")
