from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def alter_user(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha atualizada com sucesso!')
            return redirect('alter-user')
        else:
            messages.error(request, 'Erro!')
    
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'alter.html', {'form': form})