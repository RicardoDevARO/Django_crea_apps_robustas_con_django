"""# archivo de registro de rutas para la aplicación 'landing'"""

# importa las funciones necesarias para definir las rutas
from django.urls import path

# importa las vistas definidas en landing/views.py / sin este import no se podrían usar las vistas / 
# se coloca punto [ . ] para indicar que es un mismo directorio.
from . import views

#permite a Django decidir qué vista ejecutar según la URL de la petición del usuario
urlpatterns = [
    path('home', views.home, name="home"),
    path('stack/<str:tool>', views.stack_detail, name="stack_detail"),
]
