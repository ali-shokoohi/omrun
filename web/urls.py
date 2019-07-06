from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

dashbordpatterns = [
    path('', views.dashbord, name="dashbord"),
]

userpatterns = [
    path('profile/', views.profile_show, name="profile"),
    path('update/', views.profile_update, name="update"),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:pk>', views.project_detail, name="project detail"),
    path('employees/', views.employees, name="employees"),
    path('employees/<int:pk>', views.employee_detail, name="employee detail"),
    path('about/', views.about, name="about us"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.loginPage, name="login"),
    path('login-new/', views.loginPage_new, name="login new"),
    path('dashbord/', include(dashbordpatterns)),
    path('user/', include(userpatterns)),
    path('logout/', views.logoutPage, name="logout"),
    path('api/', include('web.api.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
