from typing import Any
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Team
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .forms import TeamModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q




# 1. CBV templateView
# Only need the template_name
# The get_context_data to serve the context_data
class Templateview(TemplateView):
    
    template_name = "team_view.html"


   #Context data
    # 1. self (instance of the same classe) 
    # 2. kwargs (kewords arguments): dictionary to acess all kewords passed in a function
    # 3. Super
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipes'] = Team.objects.all()
        return context
    
    
    #Post 
    #This metodo was used because CBV Method is used to show all object
    #Method used because searching function
    #Search in LV name only 
    def post(self, request):
        searching = request.POST.get('search', '')  # Use POST for search queries
        if searching:
            results = Team.objects.filter(Q(name__icontains=searching))
            if results:
                context = {'result': results}
            else:
                context = {'erro': 'Nenhum resultado encontrado.'}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, {})
        

# 2. CBV CreateView
# Requirements: model, form_class and template_name.
class CreateTeam(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamModelForm
    template_name = 'team.html'
    
     
    #Metodo de rederecionamento da urls apos o processamento
    def get_success_url(self):
        return self.request.path
    
    #Form Valid
    #Fuction to validate a form when form it;s save
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'Equipe | Criada com sucesso')
        return super().form_valid(form)
    

    #Form invalid
    #Fuction to show message when form it's invalidate
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Equipe | Erro Tente Novamente!')
        return super().form_invalid(form)
    



class Detailview(DetailView, DeleteView):
  model = Team
  template_name = 'team_detail.html'
  context_object_name = 'detail'

  def get_success_url(self):
    return reverse_lazy('Team:team_show')  # Redirecionar para a lista de equipes após a exclusão

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    details = Team.objects.filter(pk=self.kwargs.get('pk'))
    context['detail'] = details.first()  # Assumindo que você precisa apenas de um detalhe
    return context

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()

    try:
      self.object.delete()
      return HttpResponseRedirect(self.get_success_url())
    except Exception as e:
      # Gerenciar erros de exclusão (por exemplo, restrições de chave estrangeira)
      
      erros = messages.error(request, f"Erro ao excluir a equipe: {e}")
      context={
         'erro':erros
      }
      return HttpResponseRedirect(self.get_object().get_absolute_url(), context)

    
class Updateview(UpdateView):
   model = Team
   form_class = TeamModelForm
   template_name = 'team_edit.html'

   
   def get_success_url(self,*args,**kwargs):
        return reverse_lazy(
            'Team:team_detail',
             kwargs={'pk':self.kwargs.get('pk')}
        )
   
   def form_valid(self, form):
           form.save()
           messages.add_message(self.request, messages.INFO, 'Equipe | Criada com sucesso')
           #form.instance.creator = self.request.user
           return super().form_valid(form)
    
   def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Equipe | Erro Tente Novamente!')
        return super().form_invalid(form)
   

    
    


    
    


    
    





    
    
    






