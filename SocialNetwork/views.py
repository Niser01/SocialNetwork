from datetime import datetime
from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola bienvenidos a su red social")

def despedida(request):
    return HttpResponse("Hasta luego")

def Fecha(request):
    fecha_actual= datetime.datetime.now()
    return HttpResponse(fecha_actual)

def calcedad(request, annoact, annofut,edActual):
    
    periodo = annofut-annoact
    edFut = edActual+periodo
    return HttpResponse(edFut)