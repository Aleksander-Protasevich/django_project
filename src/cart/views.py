from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, RedirectView
from cart.models import Cart, GoodsInCart
from books.models import Book 
from . import utils

class CartList(DetailView):
    model = Cart
    template_name = 'cart/add-book.html'
  
    def get_object(self, *args, **kwargs):
        book_id = self.request.GET.get('book')
        current_cart_pk = self.request.session['current_cart_pk']
        if not book_id:
            current_cart_pk = self.request.session['current_cart_pk']
            if current_cart_pk:
                current_cart = Cart.objects.filter(pk = current_cart_pk).first()
                return current_cart or []
            return []
        else:
            current_cart_pk = self.request.session.get('current_cart_pk')
            current_buyer = self.request.user
            if current_buyer.is_anonymous:
                current_buyer = None
            current_cart, cart_created = Cart.objects.get_or_create(
                pk = current_cart_pk,
                defaults = {'buyer': current_buyer})
            if cart_created:
                self.request.session['current_cart_pk'] = current_cart.pk
            book = Book.objects.get(pk = book_id)
            book_in_cart, book_created = GoodsInCart.objects.get_or_create(
                cart = current_cart,
                book = book,
                defaults = {'quantity':1, 'price': book.price}
            )
            if not book_created:
                book_in_cart.quantity += 1
                book_in_cart.save()
        return current_cart

class RecalculateCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        current_cart_pk = self.request.session.get('current_cart_pk')
        if not current_cart_pk:
            return reverse('cart:add-to-cart')
        cart_items_from_form = self.request.GET
        action = utils.update_items_in_cart(cart_items_from_form, current_cart_pk)
        if action == "checkout":
            url = reverse('orders:checkout')
        else:
            url = reverse('cart:add-to-cart')
        return url
     
