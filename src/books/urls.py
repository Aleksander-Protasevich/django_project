from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.BookList.as_view(), name = 'book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name = 'book-detail'),
    path('books_by_genre/', views.BooksByGenre.as_view(), name = 'books_by_genre'),
    path('books-by-genre-detail/<int:pk>/', views.BooksByGenreDetail.as_view(), name = 'books_by_genre-detail'),

    ]
    