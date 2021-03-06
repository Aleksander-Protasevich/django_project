"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from directory import urls as directory_urls
from customer import urls as customer_urls
from books import urls as book_urls
from cart import urls as cart_urls
from orders import urls as orders_urls
from books import views as books_views

urlpatterns = [
    path('s-admin/', admin.site.urls),
    path('', books_views.HomePage.as_view(), name = 'home-page'),
    path('directory/', include(directory_urls)),
    path('customer/', include(customer_urls)),
    path('books/', include(book_urls)),
    path('cart/', include(cart_urls, namespace = 'cart')),
    path('orders/', include(orders_urls, namespace = 'orders'))
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
