from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, DeleteView
from .models import Projecto
from django.db.models import Q
from .forms import ProjectModelForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404



# 1. CBV templateView
# Only need the template_name
# The get_context_data to serve the context_data
class Templateview(TemplateView):

    template_name = 'project_view.html'


    #Context data
    # 1. self (instance of the same classe) 
    # 2. kwargs (kewords arguments): dictionary to acess all kewords passed in a function
    # 3. Super
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_projects = Projecto.objects.all()
        
        # Pagination logic
        page = self.request.GET.get('page', 1)
        paginator = Paginator(all_projects, 3)  # Show 10 teams per page
        
        try:
            projectos = paginator.page(page)
        except PageNotAnInteger:
            projectos = paginator.page(1)
        except EmptyPage:
            projectos = paginator.page(paginator.num_pages)

        context['project'] = projectos
        return context
    
    #Post 
    #This metodo was used because CBV Method is used to show all object
    #Method used because searching function
    #Search in LV name only
    def post(self, request, *args, **kwargs):
        if 'search' in request.POST:
            return self.search(request)
        elif 'delete_id' in request.POST:
            return self.delete(request, *args, **kwargs)
        else:
            return render(request, self.template_name, {})

    def search(self, request):
        searching = request.POST.get('search', '')
        if searching:
            results = Projecto.objects.filter(Q(LV__name__icontains=searching))
            if results:
                context = {'result': results}
            else:
                context = {'erro': 'Nenhum resultado encontrado.'}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, {})
    
    def delete(self, request, *args, **kwargs):
        project_id = request.POST.get('delete_id')
        project = get_object_or_404(Projecto, pk=project_id)
        try:
            project.delete()
            messages.success(request, 'Projecto deletado com sucesso.')
        except Exception as e:
            messages.error(request, f'Erro ao deletar projecto: {e}')
        return redirect(reverse_lazy('project_show'))
    

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
        return reverse_lazy('Project:project_show')
    
    #Form Valid
    #Fuction to validate a form when form it;s save
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Team | Criada com sucesso')
        #form.instance.creator = self.request.user
        return super().form_valid(form)
    
    #Form invalid
    #Fuction to show message when form it's invalidate
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Team | Erro Tente Novamente!')
        return super().form_invalid(form)
    

    


