from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from directory.models import Author, Series, Genre, Publishing
from customer.views import CustomSuccessMessageMixin
# Create your views here.

class AuthorList(LoginRequiredMixin, ListView):
    model = Author
    paginate_by = 10

class AuthorDetail(LoginRequiredMixin, DetailView):
    model = Author

class AuthorDelete(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('authors-list')
    model = Author
    
class AuthorCreate(CustomSuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Author
    success_url = reverse_lazy('authors-list')
    success_msg = 'Автор успешно создан'
    fields=('name' , 'country')
    
class AuthorUpdate(CustomSuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Author
    template_name = 'author_update.html'
    success_url = reverse_lazy('authors-list')
    success_msg = 'Автор успешно отредактирован'
    fields=('name' , 'country')   

# Seriees views

class SeriesList(LoginRequiredMixin, ListView):
    model = Series
    paginate_by = 10

class SeriesDetail(LoginRequiredMixin, DetailView):
    model = Series

class SeriesDelete(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('series-list')
    model = Series

class SeriesCreate(CustomSuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Series
    success_url = reverse_lazy('series-list')
    success_msg = 'Серия успешно создана'
    fields=('name', )
    
class SeriesUpdate(CustomSuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Series
    template_name = 'series_update.html'
    success_url = reverse_lazy('series-list')
    success_msg = 'Серия успешно отредактирована'
    fields=('name', )

# Genre views

class GenreList(LoginRequiredMixin, ListView):
    model = Genre
    paginate_by = 10

class GenreDetail(LoginRequiredMixin, DetailView):
    model = Genre

class GenreDelete(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('genre-list')
    model = Genre
    
class GenreCreate(CustomSuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Genre
    success_url = reverse_lazy('genre-list')
    success_msg = 'Жанр успешно создан'
    fields=('name', 'descr',)
    
class GenreUpdate(CustomSuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Genre
    template_name = 'genre_update.html'
    success_url = reverse_lazy('genre-list')
    success_msg = 'Жанр успешно отредактирован'
    fields=('name', 'descr',)

# Publishing views

class PublishingList(LoginRequiredMixin, ListView):
    model = Publishing
    paginate_by = 10

class PublishingDetail(LoginRequiredMixin, DetailView):
    model = Publishing

class PublishingDelete(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('publishing-list')
    model = Publishing

class PublishingCreate(CustomSuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Publishing
    success_url = reverse_lazy('publishing-list')
    success_msg = 'Издательство успешно создано'
    fields=('name', 'descr',)
    
class PublishingUpdate(CustomSuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Publishing
    template_name = 'publishing_update.html'
    success_url = reverse_lazy('publishing-list')
    success_msg = 'Издательство успешно отредактировано'
    fields=('name', 'descr', )

