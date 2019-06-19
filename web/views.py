from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from web.models import User, Employees, CommentsOfWeb, Projects
from web.forms import UserForm, EmployeesForm
#/=========================================================

#Some needed function here!

#============================Views===========================

#View of / path url
def index(request):
    employees = Employees.objects.all()#Get all employees
    comments = CommentsOfWeb.objects.all()#Get all comments
    if request.user.is_authenticated:
        has_login = True
    else:
        has_login = False
    projects_count = Projects.objects.all().count()
    employees_count = Employees.objects.all().count()
    context = {
        "employees": employees,
        "comments": comments,
        "login": has_login,
        "projects_count": projects_count,
        "employees_count": employees_count
        }
    #Open template file and pass context to that
    return render(request=request, template_name="index/index.html", context=context)

#View of login/ path url
def loginPage(request):
    #Check old sessions
    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to="/dashbord/")
    else:
        #Checking new received datas
        if request.method == 'POST':
            if ("username" in request.POST) and ("password" in request.POST):
                username = request.POST['username']
                password = request.POST['password']
                #Check authentication of login
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    #Set new session and redirect to dashboard/ url
                    #request.session['user_id'] = username
                    login(request, user)
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
    if request.user.is_authenticated:
        user = request.user
        #Get empoyee via user
        employee = Employees.objects.get(user=user)
        projects = Projects.objects.all()
        context = {
            "user": employee,
            "projects": projects,
            #...
        }
        return render(request=request, template_name="dashbord/index.html", context=context)
    else:
        #If not session is here redirect to login/ url
        return HttpResponseRedirect(redirect_to="/login/")
        
#Action of logout/ path url
def logoutPage(request):
    logout(request)
    return HttpResponseRedirect(redirect_to="/login/")

#View of user/profile/
def profile_show(request):
    if request.user.is_authenticated:
        user = request.user
        #Get empoyee via user
        employee = Employees.objects.get(user=user)
        context = {
            "user": employee,
            #...
        }
        return render(request=request, template_name="profile/index.html", context=context)
    else:
        #If not session is here redirect to login/ url
        return HttpResponseRedirect(redirect_to="/login/")

#View of user/update/
def profile_update(request):
    if request.user.is_authenticated:
        user = request.user
        #Get empoyee via user
        employee = Employees.objects.get(user=user)
        context = dict()
        context["user"] = employee
        if request.method == "GET":
            pass
        elif request.method == "POST":
            data = request.POST
            user_form = UserForm(instance=user, data=data)
            if user_form.is_valid():
                user_form.save()
                employer_form = EmployeesForm(instance=employee, data=data)
                if employer_form.is_valid():
                    employer_form.save()
                    context["message"] = "پرفایل شما با موفقیت بروزرسانی شد!"
                else:
                    context["error"] = "اطلاعات وارد شده در em صحیح نمیباشد"
                    #context["error"] = employer_form.errors
            else:
                context["error"] = "اطلاعات وارد شده در user صحیح نمیباشد"
                #context["error"] = UserForm.errors
        return render(request=request, template_name="profile/update.html", context=context)
    else:
        #If not session is here redirect to login/ url
        return HttpResponseRedirect(redirect_to="/login/")