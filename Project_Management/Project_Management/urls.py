from django.contrib import admin

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from Accounts.forms import LoginForm

# URLS IN A PROJECT


urlpatterns = [
    path('admin/', admin.site.urls),

    #path('', include('Accounts.urls')),

    path('', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name = 'login.html'), name = 'login'),

    #path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', include('Accounts.urls', namespace='logout')),

    path('team', include('Team.urls', namespace='team')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
