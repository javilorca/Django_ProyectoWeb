from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.



def servicios(request):

    servicios=Servicio.objects.all() #Orden para importar todos los servicios que haya construido
    return render(request, "servicios/servicios.html", {"servicios": servicios})