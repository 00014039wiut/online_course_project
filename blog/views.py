from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def blog_list(request):
    return render(request, 'blog.html')


def contact_page(request):
    return render(request, 'contact.html')


def blog_detail(request):
    return render(request, 'single.html')
