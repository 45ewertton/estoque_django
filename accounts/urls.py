from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name="signup"),
    path('alter/', views.alter_user , name="alter-user"),
]