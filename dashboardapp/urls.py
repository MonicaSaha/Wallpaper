"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    re_path(r'^item/(?P<category>[0-9]+)/$', views.item, name="Item"),
    re_path(r'^watch/(?P<cat>[0-9]+)/$', views.watch, name="Watch"),
    path('insert', views.insert, name='Insert'),
    path('print',views.print,name='Print'),
    path('category',views.insert_cat,name="Category")
]
