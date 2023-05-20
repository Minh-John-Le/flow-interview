from django.contrib import admin
from django.urls import path
from .views import BlogPostAPI

urlpatterns = [
 
    path('blogpost', BlogPostAPI.as_view()),
]