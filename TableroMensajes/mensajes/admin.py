from django.contrib import admin
from mensajes.models import Mensaje

class MensajeAdmin(admin.ModelAdmin):
    list_display = ("remotente", "destinatario", "texto", "fecha_hora")
    admin.site.register(Mensaje, MensajeAdmin)
    

# Register your models here.
