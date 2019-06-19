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
    path('allow-person/', views.Allow_list.as_view(), name='allow person list'),
    path('allow-person/<int:pk>/', views.Allow_detail.as_view(), name='allow person detail'),
    path('tasks/', views.Tasks_list.as_view(), name='tasks list'),
    path('tasks/<int:pk>/', views.Tasks_detial.as_view(), name='tasks detail'),
    path('todo/', views.ToDo_list.as_view(), name='todo list'),
    path('todo/<int:pk>/', views.ToDo_detail.as_view(), name='todo detail'),
    path('gallerys/', views.Gallery_list.as_view(), name='gallery list'),
    path('gallerys/<int:pk>/', views.Gallery_detial.as_view(), name='gallery detail'),
    path('photos/', views.Photos_list.as_view(), name='photos list'),
    path('photos/<int:pk>/', views.Photos_detial.as_view(), name='photos detail'),
    path('likes/', views.Likes_list.as_view(), name='likes list'),
    path('likes/<int:pk>/', views.Likes_detail.as_view(), name='likes detail'),
    path('comments/', views.Comments_list.as_view(), name='Comments list'),
    path('comments/<int:pk>/', views.Comments_detail.as_view(), name='Comments detail'),
    path('trakonesh/', views.Purchases_list.as_view(), name='trakonesh list'),
    path('trakonesh/<int:pk>/', views.Purchases_detial.as_view(), name='trakonesh detail'),
    path('projects/delete/<int:pk>/', views.Project_delete.as_view(), name='project delete'),
    path('plans/delete/<int:pk>/', views.Plan_delete.as_view(), name='plan delete')
]
urlpatterns = format_suffix_patterns(urlpatterns)