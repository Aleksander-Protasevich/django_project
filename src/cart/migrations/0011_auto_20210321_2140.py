# Generated by Django 3.1.5 on 2021-03-21 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20210227_1716'),
        ('cart', '0010_auto_20210313_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsincart',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='Книга в корзине'),
        ),
    ]
