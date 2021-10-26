from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    amount = models.IntegerField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name