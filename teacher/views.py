from django.shortcuts import render

from django.views.generic import DetailView, ListView

from teacher.models import Teacher


# Create your views here.

def teacher_list(request):
    return render(request, 'teacher/teacher.html')


class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teachers'
    template_name = 'teacher/teacher.html'


class TeacherDetailView(DetailView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'teacher/teacher-detail.html'
