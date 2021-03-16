# Generated by Django 3.1.5 on 2021-03-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20210316_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='order',
            name='contact',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Контактное лицо'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=20, verbose_name='Статус заказа'),
        ),
    ]
