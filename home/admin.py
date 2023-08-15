# Pasos para registrar los modulo


from django.contrib import admin
from .models import Department, Brand, Garment, GarmentInstance


# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    pass

# Definicion del ModelAdmin de Garment
@admin.register(Garment)
class GarmentAdmin(admin.ModelAdmin):
    pass

# # Definicion de del ModelAdmin de GarmentInstance
@admin.register(GarmentInstance) 
class GarmentInstanceAdmin(admin.ModelAdmin):
    pass 

# Instanciamos los modulos
admin.site.register(Department)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Garment)
admin.site.register(GarmentInstance)
