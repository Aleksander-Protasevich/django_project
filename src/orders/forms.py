from django import forms
from django.db.models import fields
from . import models



class CheckoutForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields=('address', 'phone', 'contact', 'comment')