from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import Author, Photo, Blog, Comment, User
from course.models import Category

# Register your models here.

admin.site.register(Author)
admin.site.register(Photo)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(User)



