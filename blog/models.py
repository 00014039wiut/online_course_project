from datetime import timezone, datetime
from tkinter import Image

from django.db import models


# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
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
    images = models.ManyToManyField(Photo)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    file_field = models.FileField(upload_to='blogs', null=True, blank=True)

    def __str__(self):
        return self.name
