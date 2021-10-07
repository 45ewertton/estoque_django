from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_company, name="home-company"),
    path('view/<int:pk>', views.unique_company, name="unique-company"),
]