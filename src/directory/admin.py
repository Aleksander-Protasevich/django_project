from django.contrib import admin
from .models import Author, Series, Genre, Publishing

# Register your models here.
admin.site.register(Author)
admin.site.register(Series)
admin.site.register(Genre)
admin.site.register(Publishing)