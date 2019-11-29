from . import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admina/', admin.site.urls),
    path('admin/',include('adminside.urls')),
    path('',include('userside.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)