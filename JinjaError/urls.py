from django.contrib import admin
from django.urls import path, include

from JinjaError.main import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # new
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
]
