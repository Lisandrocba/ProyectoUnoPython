from django import forms

class formNewTask(forms.Form):
    title = forms.CharField(label='Titulo de la tarea', max_length=200)
    description = forms.CharField(label='Descripcion de la tarea' , widget=forms.Textarea)

class formNewProject(forms.Form):
    name = forms.CharField(label='Titulo del proyecto', max_length=200)