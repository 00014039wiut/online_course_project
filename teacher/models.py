from django.db import models

# Create your models here.
from django.db import models


class Teacher(models.Model):
    class LevelChoices(models.TextChoices):
        JUNIOR = 'JUNIOR'
        MIDDLE = 'MIDDLE'
        SENIOR = 'SENIOR'
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, null=True, blank=True)
    rating = models.IntegerField(default=0 , null=True, blank=True)
    image = models.ImageField(upload_to='teachers/', null=True, blank=True)
    level = models.CharField(choices=LevelChoices.choices, default=LevelChoices.JUNIOR.value, max_length=150)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('course.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
