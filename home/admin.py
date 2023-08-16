from django.contrib import admin
from .models import Department, Brand, Garment, GarmentInstance


# Register your models here - 

class DeparmentAdmin(admin.ModelAdmin):
    list_display = ('name','date_of_creation','description')

# Definicion del ModelAdmin de Garment
@admin.register(Garment)
class GarmentAdmin(admin.ModelAdmin):
    """
    No se puede crear una vista de una lista de un campo 'ManyToManyField', para eso se debe hacer otra función. 
    """ 
    list_display = ('name_garment','size','department','summary','display_brand')

# Definicion de del ModelAdmin de GarmentInstance
@admin.register(GarmentInstance) 
class GarmentInstanceAdmin(admin.ModelAdmin):
    list_filter = ('dealer','date_stock' , 'status')

# Instanciamos los modulos
admin.site.register(Department, DeparmentAdmin)
admin.site.register(Brand)

"""
Todas son formas de registrar los modulos solo que son de formas diferentes.
"""