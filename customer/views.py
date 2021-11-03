from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Customer
from .forms import CustomerForm

# Create your views here.

class CustomerView(ListView):
    models = Customer
    template_name = 'customer.html'
    context_object_name = 'customer'
    paginate_by = 4
    queryset = Customer.objects.all()

class CreateCustomerView(SuccessMessageMixin, CreateView):
    model = Customer
    template_name = 'form_customer.html'
    form_class = CustomerForm
    success_message = "Cliente criado com sucesso!"
    success_url = reverse_lazy('customer-list')

class UpdateCustomerView(SuccessMessageMixin, UpdateView):
    model = Customer
    template_name = 'form_customer.html'
    form_class = CustomerForm
    success_message = "Cliente editado com sucesso!"
    success_url = reverse_lazy('customer-list')

class DeleteCustomerView(View):
    success_message = 'Cliente deletado com sucesso!'

    def get(self, request, *args, **kwargs):
        customer = get_object_or_404(Customer, pk=self.kwargs['pk'])
        customer.delete()
        messages.success(self.request, self.success_message)
        return redirect(reverse_lazy('customer-list'))