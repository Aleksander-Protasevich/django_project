from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .forms import AuthUserForm, RegisterUserForm, RegisterUserAddForm
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import Group
from django.views.generic.edit import ModelFormMixin 
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm



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
    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super().form_valid(form)
        
class UserProfileDetailView(DetailView):
    model = User
    template_name = 'profile-list.html'
    context_object_name = 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_data'] = UserProfile.objects.filter(user = self.request.user)
        return context

class UserUpdateView(UpdateView):
    model = User
    template_name = 'profile-update.html'
    success_url = reverse_lazy('add-profile-update')
    fields = ('first_name', 'last_name', 'email')

class UserAddUpdateView(CustomSuccessMessageMixin, UpdateView):
    model = UserProfile
    template_name = 'add-profile-update.html'
    success_url = reverse_lazy('home-page')
    success_msg = 'Данные профиля изменены'
    fields = ('phone', 'country', 'city', 'postcode', 'аddress')

class PasswordChangeView(CustomSuccessMessageMixin, PasswordChangeView):
    success_url = reverse_lazy('home-page')
    template_name = 'change-password.html'
    success_msg = 'Пароль успешно изменён'
    
    def password_change(request):
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)


   