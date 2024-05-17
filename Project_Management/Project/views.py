from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, DeleteView
from .models import Projecto
from django.db.models import Q
from .forms import ProjectModelForm
from django.urls import reverse_lazy
from django.contrib import messages



# 1. CBV templateView
# Only need the template_name
# The get_context_data to serve the context_data
class Templateview(TemplateView, DeleteView):

    template_name = 'project_view.html'


    #Context data
    # 1. self (instance of the same classe) 
    # 2. kwargs (kewords arguments): dictionary to acess all kewords passed in a function
    # 3. Super
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['project'] = Projecto.objects.all()
        return context
    
    #Post 
    #This metodo was used because CBV Method is used to show all object
    #Method used because searching function
    #Search in LV name only
    def post(self, request):
        searching = request.POST.get('search', '')  # Use POST for search queries
        if searching:
            results = Projecto.objects.filter(Q(LV__name__icontains=searching))
            if results:
                context = {'result': results}
            else:
                context = {'erro': 'Nenhum resultado encontrado.'}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, {})
    

# 2. CBV CreateView
# Requirements: model, form_class and template_name.
class Createview(CreateView):
    model = Projecto
    form_class = ProjectModelForm
    template_name = 'project.html'

    #Get_sucess_url
    #Fuction to get url when post it's processed
    #Back to All project page
    def get_success_url(self):
        return reverse_lazy('Project:project_show')
    
    #Form Valid
    #Fuction to validate a form when form it;s save
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'Team | Criada com sucesso')
        #form.instance.creator = self.request.user
        return super().form_valid(form)
    
    #Form invalid
    #Fuction to show message when form it's invalidate
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Team | Erro Tente Novamente!')
        return super().form_invalid(form)
    

    


