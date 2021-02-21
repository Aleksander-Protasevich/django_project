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
from directory import views as dir_views
from customer import views as cust_views
from books import views as book_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', dir_views.AuthorList.as_view(), name = 'authors-list'),
    path('authors/<int:pk>/', dir_views.AuthorDetail.as_view(), name = 'author-detail'),
    path('author-delete/<int:pk>/', dir_views.AuthorDelete.as_view(), name = 'author-delete'),
    path('author-create/', dir_views.AuthorCreate.as_view(), name = 'author-create'),
    path('author-update/<int:pk>/', dir_views.AuthorUpdate.as_view(), name = 'author-update'),
    # Series
    path('series/', dir_views.SeriesList.as_view(), name = 'series-list'),
    path('series/<int:pk>/', dir_views.SeriesDetail.as_view(), name = 'series-detail'),
    path('series-delete/<int:pk>/', dir_views.SeriesDelete.as_view(), name = 'series-delete'),
    path('series-create/', dir_views.SeriesCreate.as_view(), name = 'series-create'),
    path('series-update/<int:pk>/', dir_views.SeriesUpdate.as_view(), name = 'series-update'),
    # Genre
    path('genre/', dir_views.GenreList.as_view(), name = 'genre-list'),
    path('genre/<int:pk>/', dir_views.GenreDetail.as_view(), name = 'genre-detail'),
    path('genre-delete/<int:pk>/', dir_views.GenreDelete.as_view(), name = 'genre-delete'),
    path('genre-create/', dir_views.GenreCreate.as_view(), name = 'genre-create'),
    path('genre-update/<int:pk>/', dir_views.GenreUpdate.as_view(), name = 'genre-update'),
    # Publishing
    path('publishing/', dir_views.PublishingList.as_view(), name = 'publishing-list'),
    path('publishing/<int:pk>/', dir_views.PublishingDetail.as_view(), name = 'publishing-detail'),
    path('publishing-delete/<int:pk>/', dir_views.PublishingDelete.as_view(), name = 'publishing-delete'),
    path('publishing-create/', dir_views.PublishingCreate.as_view(), name = 'publishing-create'),
    path('publishing-update/<int:pk>/', dir_views.PublishingUpdate.as_view(), name = 'publishing-update'),
    # Customer
    path('login/', cust_views.UserLoginView.as_view(), name = 'login'),
    path('register/', cust_views.update_profile, name = 'register'),
    path('logout/', cust_views.LogOut.as_view(), name = 'logout'),
    path('profile/', cust_views.Profile.as_view(), name = 'profile'),
    # Books
    path('books/', book_views.BookList.as_view(), name = 'book-list'),
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
