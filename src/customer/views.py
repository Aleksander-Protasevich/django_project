from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .forms import AuthUserForm, RegisterUserForm, RegisterUserAddForm
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.views.generic.edit import ModelFormMixin 
from .models import UserProfile
from django.contrib.auth.models import User



class CustomSuccessMessageMixin:
    @property
    def succes_msg(self):
        return False
    def form_valid(self, form):
        messages.success(self.request,self.success_msg)
        return super().form_valid(form)

class UserLoginView(CustomSuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home-page')
    success_msg = "Пользователь авторизован"
    def get_success_url(self):
        return self.success_url


class UserRegisterView(CustomSuccessMessageMixin, CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('profile')
    success_msg = "Пользователь зарегистрирован. Дополните немного информации о себе"
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        aut_user.groups.add(Group.objects.get(name='Customers'))
        login(self.request, aut_user)
        return form_valid

    
class LogOut(LogoutView):
    next_page = reverse_lazy('home-page')

class UserProfileRegisterView(CustomSuccessMessageMixin, CreateView):
    template_name = 'profile.html'
    form_class = RegisterUserAddForm
    success_url = reverse_lazy('home-page')
    success_msg = "Cпасибо !!! Приятных покупок !!!"
    # def form_valid(self, form):
    #     form = super().form_valid(form)
    #     user = form.cleaned_data["user"]
    #     print(user)
    #     # form.instance.user = user
    #     # return super(UserProfileRegisterView, self).form_valid(form)
    
    

   
    







    
   