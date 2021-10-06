from django.forms import ModelForm
from product.models import Product

# Create the form class.
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'amount']