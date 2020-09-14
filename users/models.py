from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=15)

    def __str__(self):
        return self.username
