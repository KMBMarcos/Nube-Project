from django.shortcuts import render
from django.views import generic

from .models import Garment, Department, GarmentInstance


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_garments = Garment.objects.all().count()
    num_instances = GarmentInstance.objects.all().count()
    # Prendas disponibles (status = 'a')
    num_instances_available = GarmentInstance.objects.filter(status__exact="a").count()
    num_departments = (
        Department.objects.count()
    )  # El 'all()' esta implícito por defecto.

    # Para contabilizar el numero de visitas a la pagina 'index'
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    # Información dinamica a visualizar
    context = {
        "num_garments": num_garments,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_departments": num_departments,
        "num_visits": num_visits,
    }
    # Renderiza la plantilla HTML base_generic.html con los datos en la variable contexto
    return render(request, "index.html", context=context)


# Para ver la lista del modelo garment
class GarmentListView(generic.ListView):
    model = Garment
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Llame primero a la implementación base para obtener un contexto.
        context = super(GarmentListView, self).get_context_data(**kwargs)
        # Obtenga el blog del id y agréguelo al contexto.
        context["some_data"] = "Estos son solo algunos datos"
        return context


# Para ver los detalles de los objetos del modelo garment
class GarmentDetailView(generic.DetailView):
    model = Garment
    garment_detail = "garment_detail.html"


# Para la vista de la lista del modelo department
class DepartmentListView(generic.ListView):
    model = Department
    paginate_by = 10


# Para ver los detalles de los objetos del modelo department
class DepartmentDetailView(generic.DetailView):
    model = Department
    department_detail = "department_detail.html"
