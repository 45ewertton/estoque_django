from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Customer
from .forms import CustomerForm

# Create your views here.

class CustomerView(ListView):
    models = Customer
    template_name = 'customer.html'
    queryset = Customer.objects.all()
    context_object_name = 'customer'

class CreateCustomerView(CreateView):
    model = Customer
    template_name = 'form_customer.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')

class UpdateCustomerView(UpdateView):
    model = Customer
    template_name = 'form_customer.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')