# Generated by Django 3.1.5 on 2021-02-13 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0021_auto_20210213_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='genre1',
            new_name='genre',
        ),
    ]