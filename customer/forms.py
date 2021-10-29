from django.forms import ModelForm
from customer.models import Customer
from django.forms.widgets import *

# Create the form class.
class CustomerForm(ModelForm):
    
    class Meta:
        model = Customer
        widgets = {'user': HiddenInput(),}
        fields = '__all__'