from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from directory.models import Author, Series, Genre, Publishing

# Create your views here.

class AuthorList(ListView):
    model = Author

class AuthorDetail(DetailView):
    model = Author

class AuthorDelete(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('authors-list')
    model = Author

class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    success_url = reverse_lazy('authors-list')
    fields=('name' , 'country')
    
class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    template_name = 'author_update.html'
    success_url = reverse_lazy('authors-list')
    fields=('name' , 'country')   

# Seriees views

class SeriesList(LoginRequiredMixin, ListView):
    model = Series

class SeriesDetail(DetailView):
    model = Series

class SeriesDelete(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('series-list')
    model = Series

class SeriesCreate(LoginRequiredMixin, CreateView):
    model = Series
    success_url = reverse_lazy('series-list')
    fields=('name', )
    
class SeriesUpdate(LoginRequiredMixin, UpdateView):
    model = Series
    template_name = 'series_update.html'
    success_url = reverse_lazy('series-list')
    fields=('name', )

# Genre views

class GenreList(ListView):
    model = Genre

class GenreDetail(DetailView):
    model = Genre

class GenreDelete(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('genre-list')
    model = Genre

class GenreCreate(LoginRequiredMixin, CreateView):
    model = Genre
    success_url = reverse_lazy('genre-list')
    fields=('name', 'descr',)
    
class GenreUpdate(LoginRequiredMixin, UpdateView):
    model = Genre
    template_name = 'genre_update.html'
    success_url = reverse_lazy('genre-list')
    fields=('name', 'descr',)

# Publishing views

class PublishingList(ListView):
    model = Publishing

class PublishingDetail(DetailView):
    model = Publishing

class PublishingDelete(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('publishing-list')
    model = Publishing

class PublishingCreate(LoginRequiredMixin, CreateView):
    model = Publishing
    success_url = reverse_lazy('publishing-list')
    fields=('name', 'descr',)
    
class PublishingUpdate(LoginRequiredMixin, UpdateView):
    model = Publishing
    template_name = 'publishing_update.html'
    success_url = reverse_lazy('publishing-list')
    fields=('name', 'descr', )