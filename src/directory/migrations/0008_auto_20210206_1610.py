# Generated by Django 3.1.5 on 2021-02-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0007_auto_20210206_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='birth_date',
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя автора'),
        ),
    ]
