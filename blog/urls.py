from django.contrib import admin
from django.urls import path

from blog.views import *

urlpatterns = [
    path('home/', index, name='home'),
    path('blog-detail/', blog_detail, name='blog-detail'),
    path('contact/', contact_page, name='contact'),
    path('blog-list/', blog_list, name='blog-list'),


]