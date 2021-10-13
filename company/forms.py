from django.forms import ModelForm
from company.models import Company

# Create the form class.
class CompanyForm(ModelForm):
    
    class Meta:
        model = Company
        fields = ['name', 'cnpj', 'tel']