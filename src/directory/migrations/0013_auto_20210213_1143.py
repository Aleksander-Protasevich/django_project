# Generated by Django 3.1.5 on 2021-02-13 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0012_auto_20210213_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='nome',
            new_name='name',
        ),
    ]
