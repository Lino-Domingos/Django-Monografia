from django.urls import path
from .import views
app_name = 'Task'

urlpatterns = [
    path('', views.Templateview.as_view(), name='task_view'),
    path('task-create/', views.Createview.as_view(), name='task_create'),

]