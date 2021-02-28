from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from books.models import Book
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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['search_form'] = SearchForm()
    #     return context

class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'
