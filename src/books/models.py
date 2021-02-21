from django.db import models
from directory.models import Author, Series, Genre, Publishing
from PIL import Image

class Book (models.Model):
    name = models.CharField(verbose_name = 'Название книги', max_length=40)
    image = models.ImageField(upload_to='images/', verbose_name = 'Обложка', null=True)
    price = models.DecimalField(verbose_name = 'Цена BYN', max_digits=10, decimal_places=2, max_length=20)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, verbose_name ='Автор', related_name='author')
    serie = models.OneToOneField(Series, on_delete=models.CASCADE, verbose_name ='Cерия', related_name = 'serie')
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE, verbose_name ='Жанр', related_name='genre')
    year = models.CharField(verbose_name = 'Год издания', max_length=10)
    page = models.CharField(verbose_name = 'Количество страниц', max_length=15)
    binding = models.CharField(verbose_name = 'Переплет', max_length=40)
    format = models.CharField(verbose_name = 'Формат', max_length=20)
    isbn = models.CharField(verbose_name = 'ISBN', max_length=25)
    weight = models.PositiveIntegerField(verbose_name = 'Вес, гр')
    age_restr = models.CharField(verbose_name = 'Возрастные ограничения', max_length=25)
    publishing = models.OneToOneField(Publishing, on_delete=models.CASCADE, verbose_name ='Издательство', related_name = 'publishing')
    stock = models.PositiveIntegerField(verbose_name = 'В наличии, шт')
    available = models.BooleanField(verbose_name = 'Доступно для заказа', default=True)
    rating = models.PositiveIntegerField(verbose_name = 'Рейтинг (0-10)')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Дата последнего изменения')
    status = models.CharField(verbose_name = 'Статус товара', max_length=20, null=True)

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 210 or img.width > 210:
            output_size = (210, 210)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.name



