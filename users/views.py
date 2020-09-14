
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignupForm, UpdateForm


class SignUp(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def Update(request):
    upperfil = request.user
    form = UpdateForm
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('perfil')
    return render(request, 'update.html', {'upperfil':upperfil,'form':form})

def perfil(request):
    return render(request, 'perfil.html', {'perfil': perfil})

def del_perfil(request):
    delperfil = request.user
    if request.method == "POST":
       
       delperfil.delete()
       return redirect('login')
    return render(request, 'delete.html', {'delperfil': delperfil})

def update_user(request):
    form = UpdateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('perfil')
    return render(request, "update.html", {'form':form})
