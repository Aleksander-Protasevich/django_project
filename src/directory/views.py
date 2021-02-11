from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView

from directory.models import Author

# Create your views here.

# def authors_list(request):
#     authors = Author.objects.all()
#     context = {"authors" : authors}
#     return render(request, template_name="home.html", context=context)

class AuthorList(ListView):
    model = Author

# def author_detail(request, pk):
#     author = Author.objects.get(pk=pk)
#     context = {"object" : author}
#     return render(request, template_name="detail.html", context=context)

class AuthorDetail(DetailView):
    model = Author

# def author_delete(request, pk):
#     author = Author.objects.get(pk=pk)
#     message = f'Автор {author.name} удален'
#     author.delete()
#     context = {"message" : message}
#     return render(request, template_name="delete.html", context=context)

class AuthorDelete(DeleteView):
    success_url = '/authors-cbv/'
    model = Author

class AuthorCreate(CreateView):
    model = Author
    success_url = '/authors-cbv/'
    fields=('name' , 'birth_date' , 'country')
    
class AuthorUpdate(UpdateView):
    model = Author
    success_url = '/authors-cbv/'
    fields=('name' , 'birth_date' , 'country')   