from django.urls import path
from .views import CreateTeam, Templateview, Detailview
app_name = 'Team'

urlpatterns = [
    #path('detail/', DetailTeam.as_view(), name='team_list'),
     path('', Templateview.as_view(), name='team_show'),
    path('team-create/', CreateTeam.as_view(), name='team_create'),
    path('team-detail/<slug:slug>/', Detailview.as_view(), name='team_detail'),
]



