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
    path('login/', views.loginPage, name="login"),
    path('dashbord/', include(dashbordpatterns)),
    path('user/', include(userpatterns)),
    path('logout/', views.logoutPage, name="logout"),
    path('api/', include('web.api.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
