from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateField()

    def __str__(self):
        return self.nome
    

class Transacao(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField()

    def __str__(self):
        return self.descricao
    

class FluxoCaixa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    transacao = models.ForeignKey(Transacao, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.transacao}"
