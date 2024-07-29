from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from teacher.views import teacher_list

urlpatterns = [
    path('teacher-list/', teacher_list, name='teacher-list'),


]