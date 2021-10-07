from django.shortcuts import render
from .models import Company
# Create your views here.

def home_company(request):

    context = {}
    company_all = Company.objects.all()
    context = {'company': company_all}

    return render(request, 'company.html', context)