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
    path('authors/', views.AuthorList.as_view(), name = 'authors-list'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name = 'author-detail'),
    path('author-delete/<int:pk>/', views.AuthorDelete.as_view(), name = 'author-delete'),
    path('author-create/', views.AuthorCreate.as_view(), name = 'author-create'),
    path('author-update/<int:pk>/', views.AuthorUpdate.as_view(), name = 'author-update'),
    # Series
    path('series/', views.SeriesList.as_view(), name = 'series-list'),
    path('series/<int:pk>/', views.SeriesDetail.as_view(), name = 'series-detail'),
    path('series-delete/<int:pk>/', views.SeriesDelete.as_view(), name = 'series-delete'),
    path('series-create/', views.SeriesCreate.as_view(), name = 'series-create'),
    path('series-update/<int:pk>/', views.SeriesUpdate.as_view(), name = 'series-update'),
    # Genre
    path('genre/', views.GenreList.as_view(), name = 'genre-list'),
    path('genre/<int:pk>/', views.GenreDetail.as_view(), name = 'genre-detail'),
    path('genre-delete/<int:pk>/', views.GenreDelete.as_view(), name = 'genre-delete'),
    path('genre-create/', views.GenreCreate.as_view(), name = 'genre-create'),
    path('genre-update/<int:pk>/', views.GenreUpdate.as_view(), name = 'genre-update'),
    # Publishing
    path('publishing/', views.PublishingList.as_view(), name = 'publishing-list'),
    path('publishing/<int:pk>/', views.PublishingDetail.as_view(), name = 'publishing-detail'),
    path('publishing-delete/<int:pk>/', views.PublishingDelete.as_view(), name = 'publishing-delete'),
    path('publishing-create/', views.PublishingCreate.as_view(), name = 'publishing-create'),
    path('publishing-update/<int:pk>/', views.PublishingUpdate.as_view(), name = 'publishing-update'),
]
