from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from product.forms import ProductForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def product_list(request):

    context = {}
    product = Product.objects.all()

    search = request.GET.get('search')
    if search:
        product = Product.objects.filter(
            Q(pk__startswith=search) |
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(price__startswith=search) |
            Q(amount__startswith=search)
            )

    order = request.GET.get('order')
    if order:
        product = product.order_by(order) # ('-' + order)

    paginator = Paginator(product, 3)
    page = request.GET.get('page')
    product = paginator.get_page(page)

    context = {'product': product, 'order': order}

    return render(request, 'product.html', context)

@login_required
def product_view(request, pk):

    p_view = Product.objects.get(pk=pk)

    return render(request, 'view.html', {'product': p_view})

@login_required
def product_form(request):

    context = {}
    context['form'] = ProductForm()
    
    return render(request, 'forms.html', context)

@login_required
def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')

@login_required
def product_update(request,pk):
    context = {}
    p_update = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=p_update)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=p_update)

        if form.is_valid():
            form.save()
            return redirect('/')
    #Metodo GET
    else:
        context = {'form': form,'product':p_update}
        return render(request, 'update.html', context)   

@login_required
def product_delete(request, pk):
    p_delete = Product.objects.get(pk=pk)
    p_delete.delete()

    return redirect('/')