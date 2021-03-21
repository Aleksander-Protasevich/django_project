# Generated by Django 3.1.5 on 2021-03-21 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_auto_20210313_1658'),
        ('orders', '0007_order_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='Корзина'),
        ),
    ]
