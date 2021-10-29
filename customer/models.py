from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=20, unique=True)
    data_nasc = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name