
# Importacion de modulos
from django.urls import path
from . import views

# Inicializamos la view de "views"
urlpatterns = [
    path("", views.index, name="index")
]
