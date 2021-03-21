from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from books.models import Book
from books.models import Genre
from directory.models import Author
from .forms import SearchForm

# Create your views here.

class BookList(ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('query')
        query_set = super().get_queryset()
        if query:
            query_set = query_set.filter(name__icontains = query)
        return query_set
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query')
        context['search_form'] = SearchForm(initial= {'query': query})
        return context
    


class HomePage(ListView):
    model = Book
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_books'] = Book.objects.order_by('-created')[0:5]
        context['bestseller_books'] = Book.objects.all().filter(status = "Бестселлер")[0:5]
        context['sale_books'] = Book.objects.all().filter(status = "Распродажа")[0:5]
        return context


class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BooksByGenre(ListView):
    model = Genre
    template_name = 'books_by_genre.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['genres_books'] = Genre.objects.all()
    #     return context

class BooksByGenreDetail(DetailView):
    model = Genre
    template_name = 'books_by_genre_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre_books'] = Book.objects.filter(genre = self.object.pk)
        return context
