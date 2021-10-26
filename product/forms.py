from django.forms import ModelForm
from product.models import Product
from django.forms.widgets import *

# Create the form class.
class ProductForm(ModelForm):
    class Meta:
        model = Product
        widgets = {'user': HiddenInput(),}
        fields = '__all__'