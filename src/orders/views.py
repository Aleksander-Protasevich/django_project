from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView
from customer.views import CustomSuccessMessageMixin
from orders.models import Order
from cart.models import Cart
from customer.models import UserProfile
from orders.forms import CheckoutForm

# Create your views here.
class Checkout(UpdateView):
    model = Order
    template_name = 'orders/checkout.html'
    success_url = reverse_lazy('authors-list')
    success_msg = 'Заказ успешно создан'
    form_class = CheckoutForm

    def get_object(self, *args, **kwargs):
        order_id = self.request.GET.get('order')
        
        current_cart_pk = self.request.session['current_cart_pk']
        if order_id == "":
            current_cart = Cart.objects.filter(pk = current_cart_pk).first()
            current_buyer = self.request.user
            profile_data = UserProfile.objects.get(pk = current_buyer.pk)
            # phone = UserProfile.objects.get(user = current_buyer)
            contact = current_buyer.first_name
            current_order, order_created = Order.objects.get_or_create(
                cart = current_cart,
                summ = current_cart.total_summ,
                defaults = {
                    'contact':contact,
                    'address': profile_data.address,
                    'phone' : phone,
                    'comment':'-',
                    'status': 'Обрабатывается'})
            return current_order    



                

            


        #     current_cart_pk = self.request.session['current_cart_pk']
        #     if current_cart_pk:
        #         current_order = Cart.objects.filter(pk = current_cart_pk).first()
        #         return current_cart or []
        #     return []
        # else:
        #     current_cart_pk = self.request.session.get('current_cart_pk')
        #     print(current_cart_pk)
        #     current_buyer = self.request.user
        #     if current_buyer.is_anonymous:
        #         current_buyer = None
        #     current_cart, cart_created = Cart.objects.get_or_create(
        #         pk = current_cart_pk,
        #         defaults = {'buyer': current_buyer})
    #         print(cart_created, current_cart_pk)
    #         if cart_created:
    #             self.request.session['current_cart_pk'] = current_cart.pk
    #             print(self.request.session['current_cart_pk'])
    #         book = Book.objects.get(pk = book_id)
    #         book_in_cart, book_created = GoodsInCart.objects.get_or_create(
    #             cart = current_cart,
    #             book = book,
    #             defaults = {'quantity':1, 'price': book.price}
    #         )
    #         if not book_created:
    #             book_in_cart.quantity += 1
    #             book_in_cart.save()
    #     return current_cart