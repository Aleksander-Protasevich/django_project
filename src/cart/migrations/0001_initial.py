# Generated by Django 3.1.5 on 2021-03-09 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0014_auto_20210227_1716'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsInCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book', to='books.book', verbose_name='Книга в корзине')),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='Корзина')),
                ('price', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='books.book')),
            ],
        ),
    ]
