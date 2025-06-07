from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_dashboard, name='client_dashboard'),
    path('browse-articles/', views.browse_articles, name='browse_articles')
]
