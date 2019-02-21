from django.shortcuts import render
from .models import Employees, Comments


def index(request):
    employees = Employees.objects.all()
    comments = Comments.objects.all()
    context = {
        "employees": employees,
        "comments": comments,
        }
    return render(request=request, template_name="index/index.html", context=context)

