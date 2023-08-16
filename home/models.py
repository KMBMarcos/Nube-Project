from django.db import models
from django.urls import reverse
import uuid # Requerida para el registro de cada prenda en la tienda.
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.

# Author
class Brand(models.Model):
    """
    Modelo que representa la marca de la ropa (p. ej. Michael Kors, Zara, Oscar de la Renta, Forever 21, etc.).
    """
    name = models.CharField(max_length=50, help_text="Ingrese el nombre de la marca (Michael Kors, Zara, Oscar de la Renta, Forever 21, etc.)")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.name

# Book
class Garment(models.Model):
    """
    Modelo que representa la información general de la prenda.
    """

    name_garment = models.CharField(max_length=200)
    
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que una prenda de ropa tiene un solo departamento, pero el mismo departamento puede tener muchas prendas de ropa.
    # 'Department' es un string, en vez de un objeto, porque la clase Department aún no ha sido declarada.

    summary = models.TextField(max_length=1000, help_text="Ingrese una breve descripción de la prenda de ropa")

    size = models.CharField('SIZE',max_length=5, null=False)

    brand = models.ManyToManyField(Brand, help_text="Seleccione una marca para este producto")
    # ManyToManyField, porque una marca puede contener muchas prendas de ropa y una prenda de ropa puede cubrir varias marcas.
    # La clase Brand ya ha sido definida, entonces podemos especificar el objeto arriba.
    
    # Función requerida para el display de brand(ManyToManyField) en Admin
    def display_brand(self):
        """
        Crea un string para Brand. Esto es requerido para el display de Brand en Admin.
        """
        return ', '.join([ brand.name for brand in self.brand.all()[:3] ])

    # Aquí declaramos la descripción corta de 'Brand' en la vista de Admin
    display_brand.short_description = 'Brand'

    def __str__(self):
        """
        String que representa al objeto Product
        """
        return self.name_garment


    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('garment-detail', args=[str(self.id)])

# BookInstance
class GarmentInstance(models.Model):
    """
    Modelo que representa el estado de las prendas. 
    """
    id_garment = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para cada prenda de ropa en particular en toda la biblioteca")
    garment = models.ForeignKey('Garment', on_delete=models.SET_NULL, null=True)
    dealer = models.CharField(max_length=200)
    date_stock = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('u', 'Unstock'),
        ('o', 'On Shipping'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='u', help_text='Disponibilidad de la prenda')

    class Meta:
        ordering = ["date_stock"]

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return f'{self.id_garment}, {self.garment.name_garment}'

# Author
class Department(models.Model):
    """
    Modelo que representa un departamento.
    """
    name = models.CharField(max_length=100)
    date_of_creation = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('deparment-detail', args=[str(self.id)])


    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return self.name


