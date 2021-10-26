from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True) 
    cnpj = models.CharField(max_length=255, unique=True)
    tel = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name