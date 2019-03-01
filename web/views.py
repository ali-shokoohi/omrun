from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employees, Comments
from hashlib import md5
#/=========================================================

#Check authentication of login request
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

#============================Views===========================

#View of / path url
def index(request):
    employees = Employees.objects.all()#Get all employees
    comments = Comments.objects.all()#Get all comments
    context = {
        "employees": employees,
        "comments": comments,
        }
    #Open template file and pass context to that
    return render(request=request, template_name="index/index.html", context=context)

#View of login/ path url
def login(request):
    #Check old sessions
    if request.session.has_key('user_id'):
        return HttpResponseRedirect(redirect_to="/dashboard/")
    else:
        #Checking new received datas
        if request.method == 'POST':
            if ("username" in request.POST) and ("password" in request.POST):
                username = request.POST['username']
                password = request.POST['password']
                #Check authentication of login
                if logging(username, password) is True:
                    #Set new session and redirect to dashboard/ url
                    request.session['user_id'] = username
                    return HttpResponseRedirect(redirect_to="/dashboard/")
                else:
                    error = "!نام کاربری یا کلمه عبود اشتباه میباشد"
                    context = {
                        "error": error,
                    }
                    #Open template file and pass context to that
                    return render(request=request, template_name="login/login.html", context=context)
            else:
                error = "!لطفا همه فیلد ها را پر کنید"
                context = {
                    "error": error,
                }
                #Open template file and pass context to that
                return render(request=request, template_name="login/login.html", context=context)
        else:
            #Open login.html file and pass context to that
            return render(request=request, template_name="login/login.html")

#View of dashboard/ path url
def dashboard(request):
    #Check old sessions
    if request.session.has_key('user_id'):
        return HttpResponse(content="Noting yet here! <a href='/logout/'>Logout</a>")
    else:
        #If not session is here redirect to login/ url
        return HttpResponseRedirect(redirect_to="/login/")
        
#Action of logout/ path url
def logout(request):
    #Check old sessions
    if request.session.has_key('user_id'):
        del request.session['user_id']
    return HttpResponseRedirect(redirect_to="/login/")