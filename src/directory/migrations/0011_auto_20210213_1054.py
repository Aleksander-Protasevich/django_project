# Generated by Django 3.1.5 on 2021-02-13 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0010_author_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='series',
            new_name='name',
        ),
    ]
