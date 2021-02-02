from django.db import models

# Create your models here.

class Author (models.Model):
    first_author = models.CharField('Первый автор', max_length=50)
    second_author = models.CharField('Второй автор', max_length=50, blank = True)

    def __str__(self):
        return self.first_author

class Series (models.Model):
    series = models.CharField('Серия', max_length=100)
    
    def __str__(self):
        return self.series

class Genre (models.Model):
    main_genre = models.CharField('Основной жанр', max_length=100)
    
    def __str__(self):
        return self.main_genre
    
class Publishing (models.Model):
    publishing = models.CharField('Издательство', max_length=100)
    
    def __str__(self):
        return self.publishing
    
    
