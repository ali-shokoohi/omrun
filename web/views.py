from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Employees, CommentsOfWeb
from hashlib import md5
from django.contrib.auth.hashers import check_password
#/=========================================================

#Check authentication of login request
def logging(username, password):
    try:
        user_check = User.objects.filter(username=username).exists()
        if user_check is True:
            user = User.objects.get(username=username)
            pass_check = check_password(password, user.password)
            if pass_check is True:
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
    comments = CommentsOfWeb.objects.all()#Get all comments
    if request.session.has_key('user_id'):
        has_login = True
    else:
        has_login = False
    context = {
        "employees": employees,
        "comments": comments,
        "login": has_login,
        }
    #Open template file and pass context to that
    return render(request=request, template_name="index/index.html", context=context)

#View of login/ path url
def login(request):
    #Check old sessions
    if request.session.has_key('user_id'):
        return HttpResponseRedirect(redirect_to="/dashbord/")
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
                    return HttpResponseRedirect(redirect_to="/dashbord/")
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

#View of dashbord/ path url
def dashbord(request):
    #Check old sessions
    if request.session.has_key('user_id'):
        username = request.session.get('user_id')
        print("User id is:", type(username), username)
        #Get user by username (user-id)
        user = User.objects.get(username=username)#TODO: maybe user-id is fake!
        #Get empoyee via user
        employee = Employees.objects.get(user=user)
        context = {
            "user": employee,
            #...
        }
        return render(request=request, template_name="dashbord/index.html", context=context)
    else:
        #If not session is here redirect to login/ url
        return HttpResponseRedirect(redirect_to="/login/")
        
#Action of logout/ path url
def logout(request):
    #Check old sessions
    if request.session.has_key('user_id'):
        del request.session['user_id']
    return HttpResponseRedirect(redirect_to="/login/")
