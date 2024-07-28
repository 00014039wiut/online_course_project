# Generated by Django 5.0.7 on 2024-07-28 13:38

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('education', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/authors')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_email', models.EmailField(max_length=254)),
                ('file_field', models.FileField(blank=True, null=True, upload_to='blogs')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/blogs')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2024, 7, 28, 18, 38, 5, 262495))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('images', models.ManyToManyField(to='blog.photo')),
            ],
        ),
    ]
