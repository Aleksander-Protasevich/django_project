# Generated by Django 3.1.5 on 2021-02-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0017_publishing_descr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing',
            name='descr',
            field=models.CharField(max_length=100, null=True, verbose_name='Описание'),
        ),
    ]
