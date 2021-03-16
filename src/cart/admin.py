from django.contrib import admin
from .models import Cart, GoodsInCart

# Register your models here.
admin.site.register(Cart)
admin.site.register(GoodsInCart)

