# Generated by Django 3.2.7 on 2021-09-20 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_auto_20210920_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]
