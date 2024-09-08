from django.db import models
from django.utils import timezone


# Create your models here.
class Mensaje (models.Model):
    remitente = models.CharField(max_length = 300)
    destinatario = models.CharField(max_length = 300)
    texto = models.TextField()
    fecha_hora = models.DateTimeField(auto_now = True)

    # _str_ nos permite que el texto sea mas claro 
    def __str__(self):
        return f"{self.remitente} a {self.destinatario}: {self.texto}" 
  
