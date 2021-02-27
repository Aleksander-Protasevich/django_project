from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.BookList.as_view(), name = 'book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name = 'book-detail')

    ]