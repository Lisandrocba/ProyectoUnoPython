from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('home/<str:username>', views.hello),
    path('projects', views.project),
    path('task/', views.task),
]
