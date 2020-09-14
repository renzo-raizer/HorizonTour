from django.db import models
from django.contrib.auth.models import User

#class Product(models.Model):
#    description = models.CharField(max_length=100)
#    price = models.DecimalField(max_digits=9, decimal_places=2)
#    quantity = models.IntegerField()
#
#    def __str__(self):
#        return self.description


class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=15)

    def __str__(self):
        return self.username
