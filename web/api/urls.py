from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from web.api import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('login/', views.login.as_view(), name='login'),
    path('employees/', views.Employees_list.as_view(), name='employees list'),
    path('projects/', views.projects_list.as_view(), name='projects list'),
    path('projects/<int:pk>/', views.projects_detial.as_view(), name='project detail'),
    path('plans/', views.plans_list.as_view(), name='plans list'),
    path('plans/<int:pk>/', views.plans_detail.as_view(), name='plan detail'),
    path('tasks/', views.Tasks_list.as_view(), name='tasks list'),
    path('tasks/<int:pk>/', views.Tasks_detial.as_view(), name='tasks detail'),
    path('todo/', views.ToDo_list.as_view(), name='todo list'),
    path('todo/<int:pk>/', views.ToDo_detail.as_view(), name='todo detail'),
    path('projects/delete/<int:pk>/', views.Project_delete.as_view(), name='project delete'),
    path('plans/delete/<int:pk>/', views.Plan_delete.as_view(), name='plan delete')
]
urlpatterns = format_suffix_patterns(urlpatterns)