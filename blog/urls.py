from django.contrib import admin
from django.urls import path

from blog.views import *

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<int:pk>/add_comment/', CommentBlogView.as_view(), name='add-comment'),
    path('contact/', contact_page, name='contact'),
    path('blog-list/', BlogListView.as_view(), name='blog-list'),
    path('login-page/', LoginPage.as_view(), name='login'),
    path('logout-page/', logout_page, name='logout'),
    path('register-page/', RegisterFormView.as_view(), name='register'),


]