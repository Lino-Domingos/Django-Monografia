from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from .models import Projecto
from django.db.models import Q
from .forms import ProjectModelForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404



# 1. CBV templateView
# Only need the template_name
# The get_context_data to serve the context_data
# Add Permission check to view (only especific users)
class Templateview(PermissionRequiredMixin, TemplateView):
    permission_required = 'Project.view_projecto'
    template_name = 'project_view.html'

    

    def paginated(self, queryset, page_size):
        paginator = Paginator(queryset, page_size)  # Show 10 teams per page
        page = self.request.GET.get('page', 1)
        
        try:
            paginated = paginator.page(page)
        except PageNotAnInteger:
            paginated = paginator.page(1)
        except EmptyPage:
            paginated = paginator.page(paginator.num_pages)

        return paginated
    #Context data
    # 1. self (instance of the same classe) 
    # 2. kwargs (kewords arguments): dictionary to acess all kewords passed in a function
    # 3. Super
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_projects = Projecto.objects.all()
        paginated_projects = self.paginated(all_projects, 6)

        context['project'] = paginated_projects
        return context
    
    #Post 
    #This metodo was used because CBV Method is used to show all object
    #Method used because searching function
    #Search in LV name only
    def post(self, request, *args, **kwargs):
        if 'search' in request.POST:
            return self.search(request)
        else:
            return render(request, self.template_name, {})

    def search(self, request):
        searching = request.POST.get('search', '')
        if searching:
            results = Projecto.objects.filter(Q(equipe__name__icontains=searching))
            if results:
                search_projects = self.paginated(results, 5)
                context = {'project': search_projects}
            else:
                context = {'erro': 'Nenhum resultado encontrado.'}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, {{'project': self.paginate_queryset(Projecto.objects.all(), 5)}})
    
    
    

# 2. CBV CreateView
# Requirements: model, form_class and template_name.
class Createview(CreateView):
    model = Projecto
    form_class = ProjectModelForm
    template_name = 'project_create.html'

    #Get_sucess_url
    #Fuction to get url when post it's processed
    #Back to All project page
    def get_success_url(self):
        # return reverse_lazy('Project:project_show')
        return self.request.path
    
    #Form Valid
    #Fuction to validate a form when form it;s save
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Projecto| Criado com sucesso')
        #form.instance.creator = self.request.user
        return super().form_valid(form)
    
    #Form invalid
    #Fuction to show message when form it's invalidate
    def form_invalid(self, form):
        messages.ERROR(self.request, 'Projecto | Erro Tente Novamente!')
        return super().form_invalid(form)
    

class Deleteview(DeleteView):
    model = Projecto
    success_url = reverse_lazy('Project:project_show') 
    template_name = 'project_confirm_delete.html'
    

    
class Updateview(UpdateView):
   #permission_required = 'Team.change_team'
   model = Projecto
   form_class = ProjectModelForm
   template_name = 'project_edit.html'

   
  #  def get_success_url(self,*args,**kwargs):
  #       return reverse_lazy(
  #           'Team:team_detail',
  #            kwargs={'pk':self.kwargs.get('pk')}
  #       )
   
   def get_success_url(self):
       return reverse_lazy('Project:project_show')
   
   def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Projecto| Actuaizado com sucesso')
        #form.instance.creator = self.request.user
        return super().form_valid(form)
    
    #Form invalid
    #Fuction to show message when form it's invalidate
   def form_invalid(self, form):
        messages.ERROR(self.request, 'Projecto | Erro Tente Novamente!')
        return super().form_invalid(form)
    


