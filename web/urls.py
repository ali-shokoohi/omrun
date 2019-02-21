from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
