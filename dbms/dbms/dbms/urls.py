"""dbms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views 
from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "dbms"
admin.site.site_title = "dbsqlite"
admin.site.index_title = "DBSQLITE"
 
 
 
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('dbsqlite/', include('dbsqlite.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

