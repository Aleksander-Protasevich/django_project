from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from books.models import Book

# Create your views here.

class BookList(ListView):
    model = Book
    template_name = 'books_list.html'
