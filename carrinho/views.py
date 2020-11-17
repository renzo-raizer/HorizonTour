from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def carrinho(request):
    return render(request, 'carrinho.html', {'carrinho': carrinho})