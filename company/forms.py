from django.forms import ModelForm
from company.models import Company
from django.forms.widgets import *

# Create the form class.
class CompanyForm(ModelForm):
    
    class Meta:
        model = Company
        widgets = {'user': HiddenInput(),}
        fields = '__all__'