
from django.contrib.auth.models import User
from .models import Endereco
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignupForm, UpdateFormUser, UpdateFormEndereco
from django.contrib.auth.decorators import login_required

class SignUp(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

@login_required
def perfil(request):
    perfil = request.user
    return render(request, 'perfil.html', {'perfil': perfil})

@login_required
def update(request):
    perfil = request.user
    #endereco = Endereco.username.get(username=perfil)
    #print(endereco)
    form = UpdateFormUser(instance=perfil)
    #form2 = UpdateFormEndereco(instance=endereco)
    if(request.method == 'POST'):
        if perfil.is_authenticated:
            form = UpdateFormUser(request.POST, instance=perfil)
            #form2= UpdateFormEndereco(request.POST)
            if form.is_valid():
                perfil = form.save(commit=False)
                perfil.first_name = form.cleaned_data['first_name']
                perfil.last_name = form.cleaned_data['last_name']
                perfil.email = form.cleaned_data['email']
                #endereco= form2.save(commit=False)
                #endereco.CEP = form2.cleaned_data['CEP']
                #endereco.Endereco = form2.cleaned_data['endereco']
                #endereco.Numero = form2.cleaned_data['numero']
                #endereco.Complemento = form2.cleaned_data['complemento']
                #endereco.Bairro = form2.cleaned_data['bairro']
                #endereco.Cidade = form2.cleaned_data['cidade']
                #endereco.Estado = form2.cleaned_data['estado']
                perfil.save()
               #endereco.save()
                return redirect('perfil')
            else:
                return render(request, 'perfil.html', {'form': form, 'perfil' : perfil})
    elif(request.method == 'GET'):
        return render(request, 'update.html', {'form': form, 'perfil' : perfil})

@login_required
def del_perfil(request):
    delperfil = request.user

    if request.method == "POST":
       delperfil.delete()
       return redirect('login')
    return render(request, 'delete.html', {'delperfil': delperfil})
