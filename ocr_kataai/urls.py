from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import Home

urlpatterns = [
    path('',          Home.as_view(), name="home"),
    path('admin/',    admin.site.urls),
]
