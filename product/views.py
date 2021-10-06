from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from product.forms import ProductForm
# Create your views here.

def product_list(request):
    
    p_list = Product.objects.all()

    return render(request, 'product.html', {'product': p_list})

def product_view(request, pk):

    p_view = Product.objects.get(pk=pk)

    return render(request, 'view.html', {'product': p_view})

def product_form(request):

    context = {}
    context['form'] = ProductForm()
    
    return render(request, 'forms.html', context)

def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
