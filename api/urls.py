"""api URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("root/", include("app.urls"))
]
