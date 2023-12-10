from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

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