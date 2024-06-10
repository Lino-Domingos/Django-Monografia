from django.shortcuts import render
from .forms import CreateForm
from .models import Task
from django.contrib import messages
from django.db.models import Q
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# Create your views here.
# def index(request):
#     form = CreateForm()
#     return render(request,'task_view.html', {'form':form})


# def forms(request):
#     form = CreateForm()
#     return render (request, 'task_view.html', {'form':form})

class Templateview(PermissionRequiredMixin, TemplateView):
    permission_required = 'Project.view_projecto'
    template_name = 'task_view.html'


    #Funcao ou metodo para a paginacao de tarefas
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
        all_task = Task.objects.all()
        paginated_tasks = self.paginated(all_task, 8)

        context['tarefas'] = paginated_tasks
        return context
    

    def post(self, request):
        searching = request.POST.get('search', '')  # Use POST for search queries
        if searching:
            results = Task.objects.filter(Q(name__icontains=searching))
            if results.exists():
                search_tasks = self.paginated(results, 8)
                context = {'tarefas': search_tasks}
            else:
                context = {'erro': 'Nenhum resultado encontrado.'}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, { {'tarefas': self.paginate_queryset(Task.objects.all(), 8)}})
        



class Createview(PermissionRequiredMixin, CreateView):
    permission_required = 'Project.add_projecto'
    model = Task
    form_class = CreateForm
    template_name = 'task_create.html'

    #Get_sucess_url
    #Fuction to get url when post it's processed
    #Back to All project page
    def get_success_url(self):
        return self.request.path
    
    #Form Valid
    #Fuction to validate a form when form it;s save
    def form_valid(self, form):
        form.save()
        task = form.save(commit=False)
        
        # Salva a tarefa
        task.save()
        
        # Desativar o projeto
        task.project.is_active = False
        task.project.save()
        messages.success(self.request, 'A tarefa foi criada com sucesso!')
        return super().form_valid(form)
    
    #Form invalid
    #Fuction to show message when form it's invalidate
    def form_invalid(self, form):
        # messages.add_message(self.request, messages.ERROR, 'Task | Erro Tente Novamente!')
        messages.error(self.request, 'Erro! Tente novamente')
        return super().form_invalid(form)
    

    

