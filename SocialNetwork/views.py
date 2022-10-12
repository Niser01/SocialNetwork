from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.template import Template,Context
import datetime



class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido




def saludo(request):
    P1=Persona("Pepe", "Rodriguez")
    #nombre = "Juan"
    #apellido ="Perez"
    temas_curso =["Platillas", "Modelos","Formularios", "Vistas", "Despliegue App"]
    ultimo_login= datetime.datetime.now()
    plantilla_index= open("C:/Users/Nicolas/Documents/GitHub/SocialNetwork/SocialNetwork/Plantillas/index.html")
    plantilla_Template_index=Template(plantilla_index.read())
    plantilla_index.close()
    contx=Context({"nombre_persona": P1.nombre, "apellido_persona": P1.apellido, "last_login":ultimo_login, "temas":temas_curso})
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