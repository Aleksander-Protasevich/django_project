from django import forms
from django.db.models import fields
from . import models

class SearchForm(forms.Form):
    query = forms.CharField(label = "")

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields='__all__'
