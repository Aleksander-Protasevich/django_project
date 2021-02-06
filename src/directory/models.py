from django.db import models

# Create your models here.

class Author (models.Model):
    name = models.CharField('Имя автора', max_length=50)
    birth_date = models.CharField('Дата рождения', max_length=30, null=True)
    country = models.CharField('Страна', max_length=30, null=True)
    
    def __str__(self):
        return self.name
  
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
    
    
