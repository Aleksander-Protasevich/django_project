from django.db import models
from cart.models import Cart

class Order(models.Model):
    cart = models.OneToOneField(
        Cart,
        verbose_name = 'Корзина',
        on_delete = models.PROTECT)
    address = models.CharField(
        verbose_name = 'Адрес доставки',
        max_length=30,
        blank = False,
        null = False)
    phone = models.CharField(
        verbose_name = 'Телефон',
        max_length=20,
        blank = False,
        null = False)
    contact = models.CharField(
        verbose_name = 'Контактное лицо',
        max_length=20,
        blank = True,
        null = True)
    comment = models.TextField(
        verbose_name = 'Комментарий',
        blank = True,
        null = True)
    summ = models.DecimalField(
        verbose_name = 'Сумма заказа',
        max_digits=10,
        decimal_places=2,
        blank = False,
        null = False)
    status = models.CharField(
        verbose_name = 'Статус заказа',
        max_length=20,
        blank = False,
        null = False)

    def __str__(self):
        return f"Заказ № (self.pk)"