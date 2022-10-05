from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola bienvenidos a su red social")

def despedida(request):
    return HttpResponse("Hasta luego")