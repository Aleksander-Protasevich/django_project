# Generated by Django 3.1.5 on 2021-02-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20210227_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=True, verbose_name='Доступно для заказа'),
        ),
    ]
