from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('web/', include('web.urls')),
    path('admin/', admin.site.urls),
]
