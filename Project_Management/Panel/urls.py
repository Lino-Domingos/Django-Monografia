from django.urls import path
from .import views
app_name = 'Panel'

urlpatterns = [
    path('', views.painel, name="panel_main")
]