from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return render(request,"index.html")
def hola_mundo(request,username):
    
    """
    Vista que retorna un 'Hola Mundo' simple.
    """
    return HttpResponse("<h2>Hello %s </h2>" % username)

def about(request):
    """
    Vista que retorna una página de 'Acerca de'.
    """
    return HttpResponse("Acerca de: Esta es una página de información sobre nues")