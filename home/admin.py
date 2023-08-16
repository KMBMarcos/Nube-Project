from django.contrib import admin
from .models import Department, Brand, Garment, GarmentInstance


# Register your models here - 


class DeparmentAdmin(admin.ModelAdmin):
    list_display = ('name','date_of_creation','description')

# Definicion del ModelAdmin de Garment
@admin.register(Garment)
class GarmentAdmin(admin.ModelAdmin):
    pass

# Definicion de del ModelAdmin de GarmentInstance
@admin.register(GarmentInstance) 
class GarmentInstanceAdmin(admin.ModelAdmin):
    pass 

# Instanciamos los modulos
admin.site.register(Department, DeparmentAdmin)
admin.site.register(Brand)

"""
Todas son formas de registrar los modulos solo que son de formas diferentes
"""