# Generated by Django 3.1.5 on 2021-02-21 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directory', '0025_remove_author_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название книги')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, max_length=20, verbose_name='Цена BYN')),
                ('year', models.CharField(max_length=10, verbose_name='Год издания')),
                ('page', models.CharField(max_length=15, verbose_name='Количество страниц')),
                ('binding', models.CharField(max_length=40, verbose_name='Переплет')),
                ('format', models.CharField(max_length=20, verbose_name='Формат')),
                ('isbn', models.CharField(max_length=25, verbose_name='ISBN')),
                ('weight', models.PositiveIntegerField(verbose_name='Вес (гр)')),
                ('age_restr', models.CharField(max_length=25, verbose_name='Возрастные ограничения')),
                ('stock', models.PositiveIntegerField(verbose_name='В наличии')),
                ('available', models.BooleanField(default=True, verbose_name='Доступно для заказа')),
                ('rating', models.PositiveIntegerField(verbose_name='Рейтинг (0-10)')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='directory.author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='directory.genre')),
                ('publishing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='publishing', to='directory.publishing')),
                ('serie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='serie', to='directory.series')),
            ],
        ),
    ]
