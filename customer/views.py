from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

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

class DeleteCustomerView(View):

    def get(self, request, *args, **kwargs):
        customer = get_object_or_404(Customer, pk=self.kwargs['pk'])
        customer.delete()
        return redirect(reverse_lazy('customer-list'))