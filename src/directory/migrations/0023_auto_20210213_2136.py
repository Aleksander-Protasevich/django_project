# Generated by Django 3.1.5 on 2021-02-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0022_auto_20210213_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='genre',
            field=models.ManyToManyField(related_name='Жанр', to='directory.Genre'),
        ),
    ]
