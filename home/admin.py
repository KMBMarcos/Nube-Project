from typing import List, Tuple

from django.contrib import admin
from .models import Department, Brand, Garment, GarmentInstance


# Register your models here -

# Cadena de registro asosiada de Garment
class GarmentAdminInline(admin.StackedInline):
    model = Garment
    extra = 0

# ModelAdmin de 'Department'
@admin.register(Department)
class DeparmentAdmin(admin.ModelAdmin):
    # Vista de la lista de los campos de cada departamento
    list_display = ('name' , 'date_of_creation', 'description')
    # Añadiendo los campos del departamento
    field: list[str | tuple[str, str]] = ['name', ('date_of_creation', 'description')]
    inlines = [GarmentAdminInline]

# Cadena de registro asosiada de GarmentInstance
class GarmentInstanceInline(admin.StackedInline):
    model = GarmentInstance
    extra = 0

# ModelAdmin de 'Garment'
@admin.register(Garment)
class GarmentAdmin(admin.ModelAdmin):

    # No se puede crear una vista de una lista de un campo 'ManyToManyField', para eso se debe hacer otra función.

    list_display = ('name_garment', 'size', 'department', 'summary', 'display_brand')
    inlines = [GarmentInstanceInline]


# ModelAdmin de 'GarmentInstance'
@admin.register(GarmentInstance) 
class GarmentInstanceAdmin(admin.ModelAdmin):
    # Vista de la lista de campos de 'GarmentInstace'
    list_display = ('id_garment', 'garment', 'salesman', 'dealer', 'date_stock', 'status')
    # Creamos la vista del filtro
    list_filter = ('dealer', 'date_stock', 'status')

    # Cabeceras de informacion de 'Garment Instance'
    fieldsets = (
        (
            'Info', {
                'fields': ('garment', 'id_garment', 'dealer')
            }),
        ('Availability',{
            'fields': ('status', 'date_stock', 'salesman')
        }),
    )

admin.site.register(Brand)
