from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_company, name="home-company"),
    path('view/<int:pk>', views.unique_company, name="unique-company"),
    path('delete/<int:pk>', views.delete_company, name="delete-company"),
    path('update/<int:pk>', views.update_company, name="update-company"),
]