from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView, View

import blog
from blog.forms import CommentBlogForm, RegisterModelForm, LoginForm
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


def categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'base.html')


class RegisterFormView(FormView):
    template_name = 'auth/register.html'
    form_class = RegisterModelForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data['email']
        user.password = form.cleaned_data['password']

        user.save()

        login(self.request, user)
        return redirect('home')


class LoginPageView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('customers')

        return render(request, 'auth/login.html', {'form': form})


class LoginPage(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('customers')


def logout_page(request):
    logout(request)
    return redirect('home')


def contact_page(request):
    return render(request, 'home/contact.html')


def blog_detail(request):
    return render(request, 'blog/single.html')


def login_page(request):
    return render(request, 'auth/login.html')


def register_page(request):
    return render(request, 'auth/register.html')
