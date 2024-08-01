from django.shortcuts import render

from django.views.generic import ListView, TemplateView, View

from course.models import Course, Category


# Create your views here.

def course_list(request):
    return render(request, 'course/course.html')


class CourseListView(ListView):
    model = Course
    template_name = 'course/course.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = Course.objects.all()
        categories = Category.objects.all()
        context['categories'] = categories
        context['courses'] = courses
        return context


def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'course/course-detail.html', {'course': course})


def about_page(request):
    return render(request, 'home/about.html')


class AboutView(TemplateView):
    template_name = 'home/about.html'
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        return context
