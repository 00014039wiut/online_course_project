from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from course.views import *

urlpatterns = [
    path('course-list/', CourseListView.as_view(), name='course-list'),
    path('course-detail/<int:course_id>/', course_detail, name='course-detail'),
    path('about-page/', AboutView.as_view(), name='about-page'),



]