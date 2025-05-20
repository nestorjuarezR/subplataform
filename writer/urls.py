from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.writer_dashboard, name='writer_dashboard'),
    path('create-article/', views.create_article, name='create_article'),
    path('my-articles/', views.my_articles, name='my_articles'),
    path('update-article/<int:pk>/', views.update_article, name='update_article'),
]
