from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
# Create your views here.

days_of_week = {
    "monday": "Feliz lunes gusano infeliz",
    "tuesday": "Feliz martes gusano triste",
    "wednesday": "Feliz miercoles gusano aburrido",
    "thursday": "Feliz jueves gusano cansado",
    "friday": "Feliz viernes gusano emocionado",
    "saturday": "Feliz sabado gusano fiestero",
    "sunday": "Feliz domingo gusano descansado"
}

def index(request):
    days = list(days_of_week.keys())
    return render(request, "quotes/index.html", {
        "days": days
    })


def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound("<h1>El día no existe gusano tonto</h1>")
    redirect_day = days[day - 1]
    redirec_path = reverse("day-quote", args=[redirect_day])
    return HttpResponseRedirect(redirec_path)


def days_week (request, day):
    try:
        quotes_text = days_of_week[day]
        return HttpResponse(quotes_text)
    except KeyError:
        #return HttpResponseNotFound("Este día no existe gusano perdido")
        #return render(request,'404.html')
        raise Http404()