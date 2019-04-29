from django.urls import path
from web.api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('projects/', views.projects, name='projects'),
    path('plans/', views.plans, name='plans')
]