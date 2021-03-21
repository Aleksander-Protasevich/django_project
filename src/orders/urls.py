from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('checkout/', views.Checkout.as_view(), name = 'checkout'),
    path('customer-order-list/', views.CustomerOrderList.as_view(), name = 'customer-order-list'),
    path('customer-order-detail/<int:pk>/', views.CustomerOrderDetail.as_view(), name = 'customer-order-detail'),
    path('customer-order-update/<int:pk>/', views.CustomerOrderUpdate.as_view(), name = 'customer-order-update'),
    path('customer-order-delete/<int:pk>/', views.CustomerOrderDelete.as_view(), name = 'customer-order-delete'),
    path('manager-order-list/', views.ManagerOrderList.as_view(), name = 'manager-order-list'),
    path('manager-order-detail/<int:pk>/', views.ManagerOrderDetail.as_view(), name = 'manager-order-detail'),
    path('manager-order-update/<int:pk>/', views.ManagerOrderUpdate.as_view(), name = 'manager-order-update'),    
    path('manager-order-delete/<int:pk>/', views.ManagerOrderDelete.as_view(), name = 'manager-order-delete'), 
    ]
