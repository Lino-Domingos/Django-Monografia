from django.urls import path
from .import views
app_name = 'Panel'

urlpatterns = [
    path('', views.painel, name="panel_main"),
    path('mapa-view/', views.mapa, name='map'),
    path('proxy/', views.geoserver_proxy, name='geoserver_proxy'),
]
