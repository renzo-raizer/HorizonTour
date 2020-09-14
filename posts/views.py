from django.shortcuts import render
from django.http import HttpResponse
from .models import Postagens
# Create your views here.

def home (request):
    posts = Postagens.objects.all()
    return render(request, 'home.html', {'posts': posts})

def lista_produtos (request):
    posts = Postagens.objects.all()
    return render(request, 'lista_produtos.html', {'posts': posts}) 

def access_produto (request, id):
    posts = Postagens.objects.get(id=id)
    return render(request, 'produto.html', {'posts': posts})