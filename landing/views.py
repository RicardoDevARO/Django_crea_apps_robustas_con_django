# archivo que contiene las vistas de la aplicación 'landing', que manejan la lógica de las solicitudes y respuestas HTTP.
# Cada vista es una función que recibe una solicitud y devuelve una respuesta, generalmente renderizando una plantilla HTML con datos dinámicos.


# este import permite usar la función render para generar respuestas HTML
from django.shortcuts import render

# imports comentados que no se usan
# from django.http import HttpResponse
# Cierre imports comentados que no se usan

# importa la clase date del módulo datetime para trabajar con fechas
from datetime import date


# función que maneja las solicitudes a la página de inicio
def home(request):
    today = date.today()
    stack = ['Python', 'Django', 'Golang', 'PHP', 'JS']
    return render(request, "landing/landing.html", {
        "name": "Fernando",
        "today": today,
        "age": "28",
        "stack": stack
    })

