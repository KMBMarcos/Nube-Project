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

# Para ver la lista del modelo garment
class GarmentListView(generic.ListView):
    model = Garment
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # Llame primero a la implementación base para obtener un contexto.
        context = super(GarmentListView, self).get_context_data(**kwargs)
        # Obtenga el blog del id y agréguelo al contexto.
        context['some_data'] = 'Estos son solo algunos datos'
        return context

# Para ver los detalles de los objetos del modelo garment
class GarmentDetailView(generic.DetailView):
    model = Garment
    garment_detail = 'garment_detail.html'

# Para la vista de la lista del modelo department
class DepartmentListView(generic.ListView):
    model = Department
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # Llame primero a la implementación base para obtener un contexto.
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        # Obtenga el blog del id y agréguelo al contexto.
        context['some_data'] = 'Estos son solo algunos datos'
        return context

# Para ver los detalles de los objetos del modelo department
class DepartmentDetailView(generic.DetailView):
    model = Department
    department_detail = 'deparment_detail.html'