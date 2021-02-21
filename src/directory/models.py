from django.db import models

# Create your models here.

class Genre (models.Model):
    name = models.CharField('Жанр', max_length=100)
    descr = models.TextField('Описание', null=True)
    
    def __str__(self):
        return self.name

class Author (models.Model):
    name = models.CharField('Имя автора', max_length=50)
    country = models.CharField('Страна', max_length=30, null=True)
    
    def __str__(self):
        return self.name
  
class Series (models.Model):
    name = models.CharField('Серия', max_length=100)
    
    def __str__(self):
        return self.name
    
class Publishing (models.Model):
    name = models.CharField('Издательство', max_length=100)
    descr = models.CharField('Страна', max_length=100, null=True)

    def __str__(self):
        return self.name
    
    
