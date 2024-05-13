from django.urls import path
from .views import CreateTeam, Ex2View
app_name = 'Team'

urlpatterns = [
    #path('detail/', DetailTeam.as_view(), name='team_list'),
    path('ex2/', CreateTeam.as_view(), name='team_create'),
    path('', Ex2View.as_view(), name='team_show'),
]



