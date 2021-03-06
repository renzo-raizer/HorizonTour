from django.db import models
from django.utils import timezone

# Create your models here.
class Postagens(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    imagem = models.FileField(blank=True, upload_to='static/imagens')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo