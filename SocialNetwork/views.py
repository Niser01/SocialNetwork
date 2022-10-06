from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.template import Template,Context
import datetime

def saludo(request):
    plantilla_index= open("C:/Users/Nicolas/Documents/GitHub/SocialNetwork/SocialNetwork/Plantillas/index.html")
    plantilla_Template_index=Template(plantilla_index.read())
    plantilla_index.close()
    contx=Context()
    Render_index=plantilla_Template_index.render(contx)
    return HttpResponse(Render_index)

def despedida(request):
    return HttpResponse("Hasta luego")

def Fecha(request):
    fecha_actual= datetime.datetime.now()
    return HttpResponse(fecha_actual)

def calcedad(request, annoact, annofut,edActual):
    
    periodo = annofut-annoact
    edFut = edActual+periodo
    return HttpResponse(edFut)