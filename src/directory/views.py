from django.shortcuts import render
from django.http import HttpResponse

from directory.models import Author

# Create your views here.

def authors_list(request):
    authors = Author.objects.all()
    context = {"authors" : authors}
    return render(request, template_name="home.html", context=context)

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    context = {"object" : author}
    return render(request, template_name="detail.html", context=context)