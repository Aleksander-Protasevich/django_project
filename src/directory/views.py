from django.shortcuts import render
from django.http import HttpResponse

from directory.models import Author

# Create your views here.

def home_page(request):
    auth = Author.objects.last()
    context = {"auth":auth}
    return render(request, template_name="home.html", context=context)