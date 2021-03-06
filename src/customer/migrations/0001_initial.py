# Generated by Django 3.1.5 on 2021-02-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30, verbose_name='Логин')),
                ('pswrd', models.CharField(max_length=30, verbose_name='Пароль')),
                ('email', models.EmailField(max_length=30, verbose_name='E-mail')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, default='-', max_length=30, null=True, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('group', models.CharField(max_length=30, verbose_name='Группа')),
                ('country', models.CharField(blank=True, default='-', max_length=30, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, default='-', max_length=30, null=True, verbose_name='Город')),
                ('postcode', models.CharField(blank=True, default='-', max_length=10, null=True, verbose_name='Индекс')),
                ('аddress', models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='Адрес')),
            ],
        ),
    ]
