from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from web.api import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('login/', views.login.as_view(), name='login'),
    path('projects/', views.projects.as_view(), name='projects'),
    path('projects/<int:pk>/', views.projects.as_view(), name='projects'),
    path('plans/<int:pk>/', views.plans.as_view(), name='plans')
]
urlpatterns = format_suffix_patterns(urlpatterns)