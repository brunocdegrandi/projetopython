from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    pass

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10,
 decimal_places=2)

class Cliente(models.Model):
    nome = models.CharField(max_length=100)

class FormaPagamento(models.Model):
    nome = models.CharField(max_length=100)

class Venda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
