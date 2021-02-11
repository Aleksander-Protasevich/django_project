"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from directory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('authors/', views.authors_list, name = 'authors_list'),
    path('authors-cbv/', views.AuthorList.as_view(), name = 'authors-list-cbv'),
    # path('authors/<int:pk>/', views.author_detail, name = 'author_detail'),
    path('authors-cbv/<int:pk>/', views.AuthorDetail.as_view(), name = 'author-detail-cbv'),
    # path('author-delete/<int:pk>/', views.author_delete, name = 'author_delete'),
    path('author-delete-cbv/<int:pk>/', views.AuthorDelete.as_view(), name = 'author-delete-cbv'),
    path('author-create-cbv/', views.AuthorCreate.as_view(), name = 'author-create-cbv'),
    path('author-update-cbv/<int:pk>/', views.AuthorUpdate.as_view(), name = 'author-update-cbv')
]
