# Generated by Django 3.1.5 on 2021-02-21 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210221_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Обложка'),
        ),
    ]
