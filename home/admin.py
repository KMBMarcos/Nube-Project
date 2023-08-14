from django.contrib import admin
from .models import Dealer, Brand, Garment, GarmentInstance

# Register your models here.

# Instanciamos los modulos
admin.site.register(Dealer)
admin.site.register(Brand)
admin.site.register(Garment)
admin.site.register(GarmentInstance)
