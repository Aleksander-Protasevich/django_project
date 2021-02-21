from django import forms
from django.db.models import fields
from customer import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields=('username', 'password')

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=(
            'username', 'password', 'first_name',
            'last_name', 'email')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
        

class RegisterUserAddForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields=(
            'phone', 'country', 'city',
            'postcode', 'аddress')


