# Generated by Django 3.1.5 on 2021-02-13 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0011_auto_20210213_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='name',
            new_name='nome',
        ),
    ]
