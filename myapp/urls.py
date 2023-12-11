from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects', views.project, name='projects'),
    path('task/', views.task, name='tasks'),
    path('newtask/', views.newTask, name='new_task'),
    path('newproject/', views.newProject, name='new_project'),
]
