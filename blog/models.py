from datetime import timezone, datetime
from tkinter import Image

from django.db import models


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
