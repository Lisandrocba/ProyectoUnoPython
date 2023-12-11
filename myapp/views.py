from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Task
from .forms import formNewTask, formNewProject

# Create your views here.
def home(request):
    return render(request, 'index.html')

def hello(request, username):
    return HttpResponse("<h1>Hola %s</h1>" %username)

def about(request):
    return HttpResponse("<p>Hola desde about</p>")

def task(request):
    res = Task.objects.all()
    return render(request, 'task.html', {
        'tasks' : res
    })

def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {
        'projects' : projects
    })

def newTask(request):
    if request.method == 'POST':
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id = 2)
        return redirect('tasks')
    else:
        return render(request, 'newTask.html', {
            'form': formNewTask()
        })
    
def newProject(request):
    if request.method == 'POST':
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    else:
        return render(request, 'newTask.html', {
            'form': formNewProject,
        })