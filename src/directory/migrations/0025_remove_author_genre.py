# Generated by Django 3.1.5 on 2021-02-21 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0024_auto_20210214_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='genre',
        ),
    ]
