from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests

# Create your views here.

@login_required
def painel(request):
    return render(request, 'home.html')

def mapa(request):
    return render(request, 'mapa.html')

def geoserver_proxy(request):
    url = 'http://localhost:8080/geoserver/ows'
    params = request.GET.dict()  # Captura os parâmetros da solicitação GET
    response = requests.get(url, params=params)  # Faz a solicitação ao GeoServer
    return JsonResponse(response.json(), safe=False)  # Retorna a resposta como JSON