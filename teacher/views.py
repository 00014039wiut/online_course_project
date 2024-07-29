from django.shortcuts import render

# Create your views here.

def teacher_list(request):
    return render(request, 'teacher.html')