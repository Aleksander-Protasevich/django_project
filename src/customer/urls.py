from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('register/', views.UserRegisterView.as_view(), name = 'register'),
    path('logout/', views.LogOut.as_view(), name = 'logout'),
    path('profile/', views.UserProfileRegisterView.as_view(), name = 'profile'),
    path('profile-detail/<int:pk>/', views.UserProfileDetailView.as_view(), name = 'profile-detail'),
    path('profile-update/<int:pk>/', views.UserUpdateView.as_view(), name = 'profile-update'),
    path('add-profile-update/<int:pk>/', views.UserAddUpdateView.as_view(), name = 'add-profile-update'),
    path('change-password/', views.PasswordChangeView.as_view(), name = 'change-password'),



    ]


    
