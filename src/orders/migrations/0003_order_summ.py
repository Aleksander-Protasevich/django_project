# Generated by Django 3.1.5 on 2021-03-16 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='summ',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Сумма заказа'),
        ),
    ]
