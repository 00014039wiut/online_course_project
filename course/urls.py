from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from course.views import *

urlpatterns = [
    path('course-list/', course_list, name='course-list'),
    path('about-page/', about_page, name='about-page'),


]