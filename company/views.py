from django.shortcuts import render, redirect
from .models import Company
from company.forms import CompanyForm
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