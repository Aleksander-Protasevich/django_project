# Generated by Django 3.1.5 on 2021-03-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20210311_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsincart',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена BYN'),
        ),
    ]
