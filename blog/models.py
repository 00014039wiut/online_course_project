from datetime import timezone, datetime
from tkinter import Image

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from blog.managers import CustomUserManager


# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=100)

    education = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/authors')

    def __str__(self):
        return self.full_name


class Photo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/blogs')

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    images = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    birth_of_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
