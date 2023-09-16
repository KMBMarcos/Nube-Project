from django.shortcuts import render
from django.views import generic
from .models import Garment, Department, GarmentInstance


# Create your views here.


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_garments = Garment.objects.all().count()
    num_instances = GarmentInstance.objects.all().count()
    # Prendas disponibles (status = 'a')
    num_instances_available = GarmentInstance.objects.filter(status__exact="a").count()
    num_departments = Department.objects.count()  # El 'all()' esta implícito por defecto.

    # Renderiza la plantilla HTML base_generic.html con los datos en la variable contexto
    return render(
        request,
        "index.html",
        context={
            "num_garments": num_garments,
            "num_instances": num_instances,
            "num_instances_available": num_instances_available,
            "num_departments": num_departments,
        },
    )

class GarmentListView(generic.ListView):
    model = Garment
    context_object_name = 'garment_list'   # su propio nombre para la lista como variable de plantilla
    queryset = Garment.objects.filter(title__icontains='tshirt')[:5] # Consigue 5 libros que contengan el título de guerra.
    template_name = 'garments/garments_list.html'  # Especifique su propio nombre/ubicación de plantilla