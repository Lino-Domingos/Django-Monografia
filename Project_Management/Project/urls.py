from django.urls import path
from .import views
app_name = 'Project'

urlpatterns = [
    path('', views.projects, name='projectos')
]