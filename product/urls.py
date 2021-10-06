from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('view/<int:pk>/', views.product_view, name='product-view'),
]