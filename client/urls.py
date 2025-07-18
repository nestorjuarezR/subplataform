from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_dashboard, name='client_dashboard'),
    path('browse-articles/', views.browse_articles, name='browse_articles'),
    path('subscription-locked/', views.subscription_locked, name='subscription_locked'),
    path('subscription-plans/', views.subscription_plans, name='subscription_plans'),
]
