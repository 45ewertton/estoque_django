from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Customer
from .forms import CustomerForm

# Create your views here.

class CustomerView(LoginRequiredMixin, ListView):
    models = Customer
    template_name = 'customer.html'
    context_object_name = 'customer'
    paginate_by = 4
    
    def get_queryset(self):
        search = self.request.GET.get('search')
        order = self.request.GET.get('order')

        if search:
            object_list = Customer.objects.filter(
            Q(pk__startswith=search) |
            Q(name__icontains=search) |
            Q(tel__startswith=search),
            user=self.request.user
            )
        else:
            object_list = Customer.objects.filter(user=self.request.user)

        if order:
            object_list = object_list.order_by(order)

        return object_list

class CreateCustomerView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Customer
    template_name = 'form_customer.html'
    form_class = CustomerForm
    success_message = "Cliente criado com sucesso!"
    success_url = reverse_lazy('customer-list')

    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateCustomerView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Customer
    template_name = 'form_customer.html'
    form_class = CustomerForm
    success_message = "Cliente editado com sucesso!"
    success_url = reverse_lazy('customer-list')

    def form_valid(self, form):
        
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteCustomerView(LoginRequiredMixin, View):
    success_message = 'Cliente deletado com sucesso!'

    def get(self, request, *args, **kwargs):
        customer = get_object_or_404(Customer, pk=self.kwargs['pk'])
        customer.delete()
        messages.success(self.request, self.success_message)
        return redirect(reverse_lazy('customer-list'))