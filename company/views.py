from django.shortcuts import render, redirect, get_object_or_404
from company.models import Company
from company.forms import CompanyForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
# Visualizar todas as empresas, pesquisar, ordenar e criar novas empresas em um único método
def home_company(request):

    context = {}
    company = Company.objects.all().filter(user=request.user)

    search = request.GET.get('search')
    if search:
        company = Company.objects.filter(
            Q(pk__startswith=search) |
            Q(name__icontains=search) |
            Q(cnpj__startswith=search) |
            Q(tel__startswith=search),
            user=request.user
            )

    order = request.GET.get('order')
    if order:
        company = company.order_by(order) # ('-' + order)

    paginator = Paginator(company, 4)
    page = request.GET.get('page')
    company = paginator.get_page(page)

    context = {'company': company, 'order': order}
    
    context['form'] = CompanyForm()  #initial={'user': request.user}
    context['form_update'] = CompanyForm(prefix="update")

    if request.POST:
        form = CompanyForm(request.POST or None)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.info(request, 'Empresa criada com sucesso!')
            return redirect('home-company')
        else: 
            context['form'] = form
    
    return render(request, 'company.html', context)

@login_required
# Visualizar um objeto específico
def unique_company(request, pk):

    context = {}
    company_u = Company.objects.get(pk=pk)
    context = {'company': company_u}
    
    return render(request, 'unique.html', context)

@login_required
# Deletar uma empresa especifica
def delete_company(request, pk):

    comp_delete = get_object_or_404(Company, pk=pk)
    comp_delete.delete()

    messages.info(request, 'Empresa deletada com sucesso!')

    return redirect('home-company')

@login_required
# Atualizar uma empresa especifica
def update_company(request, pk):
    form = CompanyForm()
    comp_update = get_object_or_404(Company, pk=pk)
    form_update = CompanyForm()
    company_all = Company.objects.all()

    context = {'form': form_update}
    context = {'company': company_all}

    if request.method == 'POST':
        form_update = CompanyForm(request.POST, instance=comp_update)

        if form_update.is_valid():
            form_update.save()
            messages.info(request, 'Empresa atualizada com sucesso!')
            return redirect('home-company')
        else: 
            context['form'] = form
            context['form_update'] = form_update
            context['form_update_pk'] = pk

    return render(request, 'company.html', context)