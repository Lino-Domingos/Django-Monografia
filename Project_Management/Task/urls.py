from django.urls import path
from .import views
app_name = 'Task'

urlpatterns = [
    path('', views.Templateview.as_view(), name='task_view'),
    path('task-list/', views.listas.as_view(), name='task_list'),
    path('task-create/', views.Createview.as_view(), name='task_create'),
    path('task-view/',views.Taskdetailview, name='task_detail')

]