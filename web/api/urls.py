from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from web.api import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('login/', views.login.as_view(), name='login'),
    path('projects/', views.projects_list.as_view(), name='projects list'),
    path('projects/<int:pk>/', views.projects_detial.as_view(), name='project detail'),
    path('plans/', views.plans_list.as_view(), name='plans list'),
    path('plans/<int:pk>/', views.plans_detail.as_view(), name='plan detail')
]
urlpatterns = format_suffix_patterns(urlpatterns)