from django.urls import path, include

from config import settings
from teacher.views import teacher_list, TeacherDetailView, TeacherListView

urlpatterns = [
    path('teacher-list/', TeacherListView.as_view(), name='teacher-list'),
    path('teacher-detail/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),

]
