from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('view/<int:pk>/', views.product_view, name='product-view'),
    path('form/', views.product_form, name="product-form"),
    path('create/', views.product_create, name="product-create"),
    path('update/<int:pk>/', views.product_update, name="product-update"),
    path('delete/<int:pk>/', views.product_delete, name="product-delete"),
]