from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import UpdateView, ListView, DetailView, UpdateView, DeleteView
from customer.views import CustomSuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order
from cart.models import Cart
from customer.models import UserProfile
from orders.forms import CheckoutForm

# Create your views here.
class Checkout(CustomSuccessMessageMixin, UpdateView):
    model = Order
    template_name = 'orders/checkout.html'
    success_url = reverse_lazy('home-page')
    success_msg = 'Заказ успешно оформлен! Мы свяжемся с вами для уточнения данных.'
    form_class = CheckoutForm

    def get_object(self, *args, **kwargs):
        order_id = self.request.GET.get('order')
        current_cart_pk = self.request.session['current_cart_pk']
        if not order_id:
            current_cart = Cart.objects.filter(pk = current_cart_pk).first()
            current_buyer = self.request.user
            if current_buyer.is_anonymous:
                current_order, order_created = Order.objects.get_or_create(
                    cart = current_cart,
                    defaults = {
                    'address' : '-',
                    'contact': '-',
                    'phone' : '-',
                    'summ': current_cart.total_summ,
                    'comment':'-',
                    'status': 'Обрабатывается'})
                return current_order        
            else:
                current_buyer = self.request.user.profile
                phone = current_buyer.phone
                contact = self.request.user.first_name
                current_order, order_created = Order.objects.get_or_create(
                    cart = current_cart,
                    defaults = {
                    'address' : '-',
                    'contact': contact,
                    'phone' : phone,
                    'summ': current_cart.total_summ,
                    'comment':'-',
                    'status': 'Обрабатывается'})
                return current_order  
        else: 
            current_order = Order.objects.get(pk = order_id)
            return current_order
    
    def get_success_url(self):
        self.request.session['current_cart_pk'] = None
        return self.success_url    


class CustomerOrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'customer-order-list.html'
    def get_queryset(self):
       current_buyer = self.request.user
       current_buyer_carts = Cart.objects.filter(buyer = current_buyer)
       return current_buyer_carts

class CustomerOrderDetail(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'customer-order-detail.html'

class CustomerOrderUpdate(CustomSuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Order
    form_class = CheckoutForm
    template_name = 'customer-order-update.html'
    success_url = reverse_lazy('orders:customer-order-list')
    success_msg = 'Заказ успешно изменён'
    
class CustomerOrderDelete(CustomSuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'customer-order-confirm-delete.html'
    success_msg = 'Заказ успешно удален'
   
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('orders:customer-order-list')
        cart_on_delete = Cart.objects.filter(pk = self.object.pk)
        self.object.delete()
        cart_on_delete.delete()
        return HttpResponseRedirect(success_url)

class ManagerOrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'manager-order-list.html'
    
class ManagerOrderDetail(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'manager-order-detail.html'

class ManagerOrderUpdate(CustomSuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'manager-order-update.html'
    success_url = reverse_lazy('orders:manager-order-list')
    success_msg = 'Заказ успешно изменён'
    fields = ('address', 'phone', 'contact', 'comment', 'status')

class ManagerOrderDelete(CustomSuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'manager-order-confirm-delete.html'
    success_msg = 'Заказ успешно удален'
   
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('orders:manager-order-list')
        cart_on_delete = Cart.objects.filter(pk = self.object.pk)
        self.object.delete()
        cart_on_delete.delete()
        return HttpResponseRedirect(success_url)
    
    
    
        

  
                

            