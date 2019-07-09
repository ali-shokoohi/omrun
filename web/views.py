from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from web.models import User, Employees, CommentsOfWeb, Projects, Photos, NotiPerson, AllowPersons
from web.forms import UserForm, EmployeesForm, ProjectForm
#/=========================================================

#Some needed function here!

#============================Views===========================

#View of / path url
def index(request):
    employees = Employees.objects.all()#Get all employees
    comments = CommentsOfWeb.objects.all()#Get all comments
    projects_6 = Projects.objects.all().order_by("start_date")[0:5]
    if request.user.is_authenticated:
        has_login = True
    else:
        has_login = False
    projects_count = Projects.objects.all().count()
    employees_count = Employees.objects.all().count()
    context = {
        "employees": employees,
        "projects": projects_6,
        "comments": comments,
        "login": has_login,
        "projects_count": projects_count,
        "employees_count": employees_count
        }
    #Open template file and pass context to that
    return render(request=request, template_name="index/index.html", context=context)

#View of /projects/ url
def projects(request):
    if request.user.is_authenticated:
        has_login = True
    else:
        has_login = False
    projects_12 = Projects.objects.all().order_by("start_date")[0:12]
    context = {
        "projects": projects_12,
        "login": has_login
    }
    return render(request=request, template_name="index/project.html", context=context)

#View of /projects/<pk:int>/
def project_detail(request, pk):
    if request.user.is_authenticated:
        has_login = True
    else:
        has_login = False
    project = get_object_or_404(Projects, pk=pk)
    projects_3 = Projects.objects.all().order_by("start_date")[0:3]
    photos = Photos.objects.all()[0:4]
    context = {
        "project": project,
        "projects": projects_3,
        "photos": photos,
        "login": has_login
    }
    return render(request=request, template_name="index/project-single.html", context=context)

#View of /about/ url
def about(request):
    employees = Employees.objects.all()#Get all employees
    if request.user.is_authenticated:
        has_login = True
    else:
        has_login = False
    context = {
        "employees": employees,
        "login": has_login,
        }
    #Open template file and pass context to that
    return render(request=request, template_name="index/about.html", context=context)

#View of /services/ url
def services(request):
    employees = Employees.objects.all()#Get all employees
    comments = CommentsOfWeb.objects.all()#Get all comments
    projects_3 = Projects.objects.all().order_by("start_date")[0:3]
    if request.user.is_authenticated:
        has_login = True
    else:
        has_login = False
    context = {
        "employees": employees,
        "comments": comments,
        "projects": projects_3,
        "login": has_login,
        }
    #Open template file and pass context to that
    return render(request=request, template_name="index/services.html", context=context)
#View of /employees/ url
def employees(request):
    employees = Employees.objects.all()#Get all employees
    if request.user.is_authenticated:
        has_login = True
    else:
        has_login = False
    context = {
        "employees": employees,
        "login": has_login,
        }
    #Open template file and pass context to that
    return render(request=request, template_name="index/employee.html", context=context)

#View of /employees/<pk:int>/
def employee_detail(request, pk):
    if request.user.is_authenticated:
        has_login = True
    else:
        has_login = False
    employees = Employees.objects.all()#Get all employees
    employee = get_object_or_404(Employees, pk=pk)
    project_count = AllowPersons.objects.filter(user=employee.user).count()
    context = {
        "employee": employee,
        "employees": employees,
        "project_count": project_count,
        "login": has_login
    }
    return render(request=request, template_name="index/employee-single.html", context=context)


#View of /contact/ url
def contact(request):
    if request.user.is_authenticated:
        has_login = True
    else:
        has_login = False
    context = {
        "login": has_login
    }
    return render(request=request, template_name="index/contact.html", context=context)

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

#View of login-new/ path url
def loginPage_new(request):
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
                    return render(request=request, template_name="login/login-new.html", context=context)
            else:
                error = "!لطفا همه فیلد ها را پر کنید"
                context = {
                    "error": error,
                }
                #Open template file and pass context to that
                return render(request=request, template_name="login/login-new.html", context=context)
        else:
            #Open login.html file and pass context to that
            return render(request=request, template_name="login/login-new.html")

#View of dashbord/ path url
def dashbord(request):
    #Check old sessions
    if request.user.is_authenticated:
        user = request.user
        #Get empoyee via user
        employee = Employees.objects.get(user=user)
        projects = Projects.objects.all()
        notiperson = NotiPerson.objects.filter(person=user).order_by("notify.time")
        context = {
            "user": employee,
            "projects": projects,
            "notifications": notiperson,
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
        context = dict()
        context["user"] = user
        if request.method == "GET":
            pass
        elif request.method == "POST":
            data = request.POST
            data._mutable = True
            data["username"] = user.username
            data["post"] = user.post
            user_form = UserForm(instance=user, data=data)
            if user_form.is_valid():
                user_form.save()
                context["message"] = "پرفایل شما با موفقیت بروزرسانی شد!"
            else:
                context["error"] = user_form.errors
                #context["error"] = UserForm.errors
        return render(request=request, template_name="profile/update.html", context=context)
    else:
        #If not session is here redirect to login/ url
        return HttpResponseRedirect(redirect_to="/login/")

#View of /dashbord/project/view/<int:pk>
def project_show(request, pk):
    if request.user.is_authenticated:
        project = get_object_or_404(Projects, pk=pk)
        context = {
            "project": project,
            #...
        }
        return render(request=request, template_name="projects/index.html", context=context)
    else:
        #If not session is here redirect to login/ url
        return HttpResponseRedirect(redirect_to="/login/")

#View of /dashbord/project/update/<int:pk>
def project_update(request, pk):
    if request.user.is_authenticated:
        user = request.user
        employees = Employees.objects.all()#Get all employees
        project = get_object_or_404(Projects, pk=pk)
        context = dict()
        context["user"] = user
        if request.method == "GET":
            context["project"] = project
            context["employees"] = employees
        elif request.method == "POST":
            data = request.POST
            project = get_object_or_404(Projects, pk=pk)
            project_form = UserForm(instance=project, data=data)
            if project_form.is_valid():
                project_form.save()
                context["message"] = f"پروژه ی {project.name} با موفقیت بروزرسانی شد!"
            else:
                context["error"] = project_form.errors
        return render(request=request, template_name="projects/update.html", context=context)
    else:
        #If not session is here redirect to login/ url
        return HttpResponseRedirect(redirect_to="/login/")

#View of /dashbord/project/create/
def project_create(request):
    if request.user.is_authenticated:
        user = request.user
        employees = Employees.objects.all()#Get all employees
        context = dict()
        context["user"] = user
        if request.method == "GET":
            context["employees"] = employees
        elif request.method == "POST":
            data = request.POST
            project_form = UserForm(data=data)
            if project_form.is_valid():
                project_form.save()
                context["message"] = f"پروژه ی {project.name} با موفقیت ایجاد شد!"
            else:
                context["error"] = project_form.errors
        return render(request=request, template_name="projects/create.html", context=context)
    else:
        #If not session is here redirect to login/ url
        return HttpResponseRedirect(redirect_to="/login/")