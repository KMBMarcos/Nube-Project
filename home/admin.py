from django.contrib import admin
from .models import Department, Brand, Garment, GarmentInstance

# Register your models here.

# Instanciamos los modulos
admin.site.register(Department)
admin.site.register(Brand)
admin.site.register(Garment)
admin.site.register(GarmentInstance)
