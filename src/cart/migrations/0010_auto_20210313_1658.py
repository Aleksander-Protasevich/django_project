# Generated by Django 3.1.5 on 2021-03-13 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_auto_20210313_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsincart',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='cart.cart', verbose_name='Корзина'),
        ),
    ]