from django.shortcuts import render


# Create your views here.

def course_list(request):
    return render(request, 'course.html')

def about_page(request):
    return render(request, 'about.html')
