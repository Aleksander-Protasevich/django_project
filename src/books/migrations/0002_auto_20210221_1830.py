# Generated by Django 3.1.5 on 2021-02-21 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0025_remove_author_genre'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='directory.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='directory.genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishing',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='publishing', to='directory.publishing', verbose_name='Издательство'),
        ),
        migrations.AlterField(
            model_name='book',
            name='serie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='serie', to='directory.series', verbose_name='Cерия'),
        ),
    ]
