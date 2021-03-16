from django.db import models
from django.contrib.auth.models import User
from books.models import Book
# Create your models here.

class Cart(models.Model):
    buyer = models.ForeignKey(
        User,
        on_delete = models.PROTECT,
        blank = False,
        null = True
    )

    def __str__(self):
        return f" Корзина № {self.pk}"

    @property
    def total_summ(self):
        all_goods = self.goods.all()
        total = 0
        for book in all_goods:
            total += book.total_price
        return total


class GoodsInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name = "Корзина",
        on_delete=models.CASCADE,
        related_name = 'goods')
    book = models.ForeignKey(
        Book,
        verbose_name = "Книга в корзине",
        on_delete = models.PROTECT,
    )
    quantity = models.PositiveIntegerField(
        verbose_name = "Количество",
        default = 1)
    price = models.DecimalField(
        verbose_name = 'Цена BYN',
        max_digits=10,
        decimal_places=2)
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name = 'Дата создания корзины',
        null = False)
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name = 'Дата последнего изменения корзины',
        null = False)
    
    def __str__(self):
        return f" Товары в корзине № {self.pk}, {self.book.name} в количестве {self.quantity} шт."

    @property
    def total_price(self):
        return self.book.price * self.quantity
