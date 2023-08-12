from django.db import models

# Create your models here.
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
