from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerView.as_view(), name='customer-list'),
    path('create/', views.CreateCustomerView.as_view(), name='create-list'),
    path('<int:pk>/update/', views.UpdateCustomerView.as_view(), name='update-list'),
]