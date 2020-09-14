
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignupForm, UpdateForm
from django.contrib.auth.decorators import login_required

class SignUp(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

@login_required
def perfil(request):
    return render(request, 'perfil.html', {'perfil': perfil})

@login_required
def update(request):
    perfil = request.user
    form = UpdateForm(instance=perfil)
    if(request.method == 'POST'):
        form = UpdateForm(request.POST, instance=perfil)
        
        if(form.is_valid()):
            perfil = form.save(commit=False)
            perfil.first_name = form.cleaned_data['first_name']
            perfil.last_name = form.cleaned_data['last_name']
            perfil.email = form.cleaned_data['email']
            perfil.save()
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
