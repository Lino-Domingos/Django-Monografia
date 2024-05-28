from django.shortcuts import render
from .forms import CreateForm
from .models import Task
from django.contrib import messages
from django.views.generic import CreateView



# Create your views here.
def index(request):
    form = CreateForm()
    return render(request,'task_view.html', {'form':form})


def forms(request):
    form = CreateForm()
    return render (request, 'task_view.html', {'form':form})




class Createview(CreateView):
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
        # messages.add_message(self.request, messages.SUCCESS, 'Task | Created Sucessufly')
        #form.instance.creator = self.request.user
        return super().form_valid(form)
    
    #Form invalid
    #Fuction to show message when form it's invalidate
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Task | Erro Tente Novamente!')
        return super().form_invalid(form)
    

    

