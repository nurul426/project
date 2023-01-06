"""perikanan URL Configuration

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
from django.urls import path
from perikanan_app.views import *
from django.conf import settings
from django.conf.urls.static import static
from perikanan_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lokasi/", lokasi),
    path("tambahlokasi/", tambahlokasi),
    path("lokasi/editlokasi/<int:id>", editlokasi, name='editlokasi'),
    path("lokasi/hapuslokasi/<int:id>", hapuslokasi),
    path("produksi/", produksi),
    path("tambahproduksi/", tambahproduksi),
    path("produksi/editproduksi/<int:id>", editproduksi, name='editproduksi'),
    path("produksi/hapusproduksi/<int:id>", hapusproduksi),
    path("login/", views.Pagelogin, name='login'),
    path("signup/", views.Pagesignup, name='regis'),
    path("logout/", views.Pagelogout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
