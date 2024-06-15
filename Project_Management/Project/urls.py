from django.urls import path
from .import views
app_name = 'Project'

urlpatterns = [
    path('', views.Templateview.as_view(), name='project_show'),
    path('project-create/', views.Createview.as_view(), name='project_create'),
    path('project-delete/<int:pk>/delete/', views.Deleteview.as_view(), name='project_delete'),
    path('project-update/<int:pk>/update/', views.Updateview.as_view(), name='project_update'),
]