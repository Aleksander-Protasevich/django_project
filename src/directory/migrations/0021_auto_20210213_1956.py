# Generated by Django 3.1.5 on 2021-02-13 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0020_auto_20210213_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='genre',
            new_name='genre1',
        ),
    ]
