from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('news/', views.news, name="news"),
    path('news/article/<slug>/', views.news_detail, name="news-detail"),
]
