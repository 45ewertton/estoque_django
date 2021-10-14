from django.shortcuts import render, redirect, get_object_or_404
from company.models import Company
from company.forms import CompanyForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

# Visualizar todas as empresas e criar novas empresas em um único método
def home_company(request):

    context = {}
    company_all = Company.objects.all()

    paginator = Paginator(company_all, 4)
    page = request.GET.get('page')
    company = paginator.get_page(page)

    context = {'company': company}
    
    context['form'] = CompanyForm()
    context['form_update'] = CompanyForm(prefix="update")

    if request.POST:
        form = CompanyForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.info(request, 'Empresa criada com sucesso!')
            return redirect('home-company')
        else: 
            context['form'] = form
    
    return render(request, 'company.html', context)

# Visualizar um objeto específico
def unique_company(request, pk):

    context = {}
    company_u = Company.objects.get(pk=pk)
    context = {'company': company_u}
    
    return render(request, 'unique.html', context)

# Deletar uma empresa especifica
def delete_company(request, pk):

    comp_delete = get_object_or_404(Company, pk=pk)
    comp_delete.delete()

    messages.info(request, 'Empresa deletada com sucesso!')

    return redirect('home-company')

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
