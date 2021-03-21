from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.BookList.as_view(), name = 'book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name = 'book-detail'),
    path('books_by_genre/', views.BooksByGenre.as_view(), name = 'books_by_genre'),
    path('books-by-genre-detail/<int:pk>/', views.BooksByGenreDetail.as_view(), name = 'books_by_genre-detail'),
    path('manager-book-list/', views.ManagerBookList.as_view(), name = 'manager-book-list'),
    path('manager-book-update/<int:pk>/', views.ManagerBookUpdate.as_view(), name = 'manager-book-update'),
    path('manager-book-create/', views.ManagerBookCreate.as_view(), name = 'manager-book-create'),
    path('manager-book-delete/<int:pk>/', views.ManagerBookDelete.as_view(), name = 'manager-book-delete')

    ]
    