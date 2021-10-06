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

def product_update(request,pk):
    context = {}
    p_update = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=p_update)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=p_update)

        if form.is_valid():
            p_update.save()
            return redirect('/')
    #Metodo GET
    else:
        context = {'form': form,'product':p_update}
        return render(request, 'update.html', context)   

def product_delete(request, pk):
    p_delete = Product.objects.get(pk=pk)
    p_delete.delete()
    return redirect('/')
