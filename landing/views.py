# archivo que contiene las vistas de la aplicación 'landing', que manejan la lógica de las solicitudes y respuestas HTTP.
# Cada vista es una función que recibe una solicitud y devuelve una respuesta, generalmente renderizando una plantilla HTML con datos dinámicos.


# este import permite usar la función render para generar respuestas HTML
from django.shortcuts import render

# imports comentados que no se usan
from django.http import HttpResponse
# Cierre imports comentados que no se usan

# importa la clase date del módulo datetime para trabajar con fechas
from datetime import date


# función que maneja las solicitudes a la página de inicio
def home(request):
    today = date.today()
    stack = [{'id': 'python', 'name':'Python'}, {'id': 'django', 'name':'Django'}, {'id': 'js', 'name':'JavaScript'}, {'id': 'react', 'name':'React'}]
    return render(request, "landing/landing.html", {
        "name": "Fernando",
        "today": today,
        "age": "28",
        "stack": stack
    })


def stack_detail(request, tool):
    return HttpResponse(f"Tecnología: {tool}")