# Generated by Django 3.1.5 on 2021-01-31 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_auto_20210131_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_genre', models.CharField(max_length=100, verbose_name='Основной жанр')),
            ],
        ),
        migrations.CreateModel(
            name='Publishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishing', models.CharField(max_length=100, verbose_name='Издательство')),
            ],
        ),
    ]
