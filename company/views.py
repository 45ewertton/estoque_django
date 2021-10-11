from django.shortcuts import render, redirect, get_object_or_404
from .models import Company
from company.forms import CompanyForm
from django.contrib import messages
# Create your views here.

# Visualizar todas as empresas e criar novas empresas em um único método
def home_company(request):

    context = {}
    company_all = Company.objects.all()
    context = {'company': company_all}
    context['form'] = CompanyForm()

    if request.POST:
        form = CompanyForm(request.POST or None)
        if form.is_valid():
            form.save()
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
    comp_update = get_object_or_404(Company, pk=pk)
    form = CompanyForm(instance=comp_update)
    context = {'form': form}

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=comp_update)

        if form.is_valid():
            form.save()
            return redirect('home-company')
    else:
        return redirect('home-company')