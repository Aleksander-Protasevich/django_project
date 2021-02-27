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
    next_page = reverse_lazy('authors-list')

class UserProfileRegisterView(CustomSuccessMessageMixin, CreateView):
    template_name = 'profile.html'
    form_class = RegisterUserAddForm
    success_url = reverse_lazy('home-page')
    success_msg = "Cпасибо !!! Приятных покупок !!!"
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        form_valid.user = self.request.user
        form_valid.save()
        return form_valid
    
    

   
    







    
    # form_class = RegisterUserForm
    # def get_context_data(self, **kwargs):
    #     context = super(Profile, self).get_context_data(**kwargs)
    #     context['username'] = self.request.user.username
    #     return context


# def update_profile(request):
#     if request.method == 'POST':
#         user_form = RegisterUserForm(request.POST, instance=request.user)
#         profile_form = RegisterUserAddForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             # username = user_form.cleaned_data["username"]
#             # password = user_form.cleaned_data["password"]
#             # aut_user = authenticate(username=username, password=password)
#             # aut_user.groups.add(Group.objects.get(name='Customers'))
#             # login(request, aut_user)
#             # messages.success(request, 'Registration complete! You may log in!')
#             return redirect('authors-list')
#         else:
#             messages.error(request, ('Пожалуйста исправьте ошибки'))
#     else:
#         user_form = RegisterUserForm(instance=request.user)
#         profile_form = RegisterUserAddForm(instance=request.user.profile)
#     return render(request, 'register.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })



# def update_profile(request):
#     if request.method == 'POST':
#         user_form = RegisterUserForm(request.POST)
#         profile_form = RegisterUserAddForm(request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             profile_form = profile_form.save(commit=False)
#             profile_form.save
#             username = user_form.cleaned_data["username"]
#             password = user_form.cleaned_data["password"]
#             aut_user = authenticate(username=username, password=password)
#             aut_user.groups.add(Group.objects.get(name='Customers'))
#             login(request, aut_user)
#             messages.success(request, 'Registration complete! You may log in!')
#             return redirect('authors-list')
#         else:
#             messages.error(request, ('Пожалуйста исправьте ошибки'))
#     else:
#         user_form = RegisterUserForm(request.POST)
#         profile_form = RegisterUserAddForm(request.POST)
#     return render(request, 'register.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })