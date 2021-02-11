from django import forms
from django.db.models import fields
from . import models

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields=('name' , 'birth_date' , 'country')

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name == "Alex":
            self.add_error('name', 'Это имя недопустимо')
        return cleaned_data
    
    
    