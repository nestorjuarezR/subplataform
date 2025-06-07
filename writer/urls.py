from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.writer_dashboard, name='writer_dashboard'),
    path('create-article/', views.create_article, name='create_article'),
    path('my-articles/', views.my_articles, name='my_articles'),
    path('update-article/<int:pk>/', views.update_article, name='update_article'),
    path('delete-article/<int:pk>/', views.delete_article, name='delete_article'),
    path('account-management/', views.account_management, name='account_management'),
    path('delete-account/', views.delete_account, name='delete_account'),
]
