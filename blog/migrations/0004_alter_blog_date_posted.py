# Generated by Django 5.0.7 on 2024-07-31 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 31, 16, 50, 13, 931659)),
        ),
    ]
