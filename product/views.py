from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
# Create your views here.

def product_list(request):
    
    p_list = Product.objects.all()

    return render(request, 'product.html', {'product': p_list})

def product_view(request, pk):

    p_view = Product.objects.get(pk=pk)

    return render(request, 'view.html', {'product': p_view})