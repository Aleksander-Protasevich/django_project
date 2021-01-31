from django.db import models

# Create your models here.

class Author (models.Model):
    first_author = models.CharField('Первый автор', max_length=50)
    second_author = models.CharField('Второй автор', max_length=50, blank = True)

class Series (models.Model):
    series = models.CharField('Серия', max_length=100)
    
class Genre (models.Model):
    main_genre = models.CharField('Основной жанр', max_length=100)
    
class Publishing (models.Model):
    publishing = models.CharField('Издательство', max_length=100)
    