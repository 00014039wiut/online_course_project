from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

import blog
from blog.forms import CommentBlogForm
from blog.models import Blog, Author
from course.models import Category, Course, Comment
from teacher.models import Teacher


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['courses'] = Course.objects.all()
        courses_of_category = {category: category.courses.all() for category in Category.objects.all()}
        context['blogs'] = Blog.objects.all()
        context['teachers'] = Teacher.objects.all()
        context['courses_of_category'] = courses_of_category

        return context


def blog_list(request):
    return render(request, 'blog/blog.html')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['courses'] = Course.objects.all()
        context['blogs'] = Blog.objects.all()
        context['teachers'] = Teacher.objects.all()
        context['authors'] = Author.objects.all()
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/single.html'
    context_object_name = 'blog'


class CommentBlogView(TemplateView):
    template_name = 'blog/single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_id = self.kwargs.get('blog_id')
        context['blog'] = get_object_or_404(Blog, id=blog_id)
        context['form'] = CommentBlogForm()
        return context

    def post(self, request, *args, **kwargs):
        blog_id = self.kwargs.get('blog_id')
        blog = get_object_or_404(Blog, id=blog_id)
        form = CommentBlogForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_id = blog
            comment.name = form.cleaned_data['name']
            comment.email = form.cleaned_data['email']
            comment.content = form.cleaned_data['content']
            comment.author = form.cleaned_data['author']
            comment.save()
            return redirect(reverse('blog-detail', kwargs={'pk': blog_id}))
        return self.render_to_response(self.get_context_data(form=form, blog=blog))


def contact_page(request):
    return render(request, 'home/contact.html')


def blog_detail(request):
    return render(request, 'blog/single.html')


def login_page(request):
    return render(request, 'auth/login.html')


def register_page(request):
    return render(request, 'auth/register.html')
