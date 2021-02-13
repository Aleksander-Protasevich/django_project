from django import forms
from django.db.models import fields
from . import models

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields=('name', 'genre', 'country')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get('name')
    #     if name == "Alex":
    #         self.add_error('name', 'Это имя недопустимо')
    #     return cleaned_data
    

class SeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields=('name',)

class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields=('name', 'descr',)

class PublishingForm(forms.ModelForm):
    class Meta:
        model = models.Publishing
        fields=('name',)

   