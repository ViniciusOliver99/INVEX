from django.db import models
from django.views.generic.base import TemplateView
import datetime


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)


class HomePageView(TemplateView):
    template_name = "display_form.html"


class Transacao(models.Model):
    data = models.DateTimeField
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
