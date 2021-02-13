from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView

from directory.models import Author, Series, Genre, Publishing

# Create your views here.

# def authors_list(request):
#     authors = Author.objects.all()
#     context = {"authors" : authors}
#     return render(request, template_name="home.html", context=context)

# def author_detail(request, pk):
#     author = Author.objects.get(pk=pk)
#     context = {"object" : author}
#     return render(request, template_name="detail.html", context=context)

# def author_delete(request, pk):
#     author = Author.objects.get(pk=pk)
#     message = f'Автор {author.name} удален'
#     author.delete()
#     context = {"message" : message}
#     return render(request, template_name="delete.html", context=context)
class AuthorList(ListView):
    model = Author

class AuthorDetail(DetailView):
    model = Author

class AuthorDelete(DeleteView):
    success_url = '/authors/'
    model = Author

class AuthorCreate(CreateView):
    model = Author
    success_url = '/authors/'
    fields=('name' , 'genre' , 'country')
    
class AuthorUpdate(UpdateView):
    model = Author
    success_url = '/authors/'
    fields=('name' , 'genre' , 'country')   

# Seriees views

class SeriesList(ListView):
    model = Series

class SeriesDetail(DetailView):
    model = Series

class SeriesDelete(DeleteView):
    success_url = '/series/'
    model = Series

class SeriesCreate(CreateView):
    model = Series
    success_url = '/series/'
    fields=('name', )
    
class SeriesUpdate(UpdateView):
    model = Series
    success_url = '/series/'
    fields=('name', )

# Genre views

class GenreList(ListView):
    model = Genre

class GenreDetail(DetailView):
    model = Genre

class GenreDelete(DeleteView):
    success_url = '/genre/'
    model = Genre

class GenreCreate(CreateView):
    model = Genre
    success_url = '/genre/'
    fields=('name', 'descr',)
    
class GenreUpdate(UpdateView):
    model = Genre
    success_url = '/genre/'
    fields=('name', 'descr',)

# Publishing views

class PublishingList(ListView):
    model = Publishing

class PublishingDetail(DetailView):
    model = Publishing

class PublishingDelete(DeleteView):
    success_url = '/publishing/'
    model = Publishing

class PublishingCreate(CreateView):
    model = Publishing
    success_url = '/publishing/'
    fields=('name', )
    
class PublishingUpdate(UpdateView):
    model = Publishing
    success_url = '/publishing/'
    fields=('name', )