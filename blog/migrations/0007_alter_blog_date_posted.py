# Generated by Django 5.0.7 on 2024-07-31 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_date_posted_remove_blog_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 31, 21, 24, 19, 283116)),
        ),
    ]
