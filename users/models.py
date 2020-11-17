from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Endereco(models.Model):
    username = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    CEP = models.CharField(max_length=9)
    endereco= models.CharField(max_length=100)
    numero= models.CharField(max_length=8)
    complemento= models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=40)
    estado = models.CharField(max_length=30) 
    
    def __str__(self):
        return str(self.username)
