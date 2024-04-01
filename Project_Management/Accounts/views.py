

from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django.contrib import messages 



def login_view(request):
    form = LoginForm(request.POST or None)


    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                form = LoginForm()
                return redirect(reverse('team:team'))
            else:
                form = LoginForm()
                messages.error(request,('Username e/ou password incorrecto'))
        else:
            messages.error(request,('Error'))           
   
    return render(request, 'login.html', {"form": form})

    #Form passa o atributo form para o formulario no Html
            
   
