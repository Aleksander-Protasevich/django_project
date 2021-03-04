from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('register/', views.UserRegisterView.as_view(), name = 'register'),
    path('logout/', views.LogOut.as_view(), name = 'logout'),
    path('profile/', views.UserProfileRegisterView.as_view(), name = 'profile')

    ]


    
