from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerView.as_view(), name='customer-list'),
    path('create/', views.CreateCustomerView.as_view(), name='create-list'),
]