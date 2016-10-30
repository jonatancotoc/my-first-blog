from django.shortcuts import render

#librería para manejar el envío de mensajes

from django.contrib import messages
from .forms import EstudianteForm
from blog.models import Estudiante, Curso


#Vista para insertar una nueva película y los actores que actúan en ella.

def estudiante_nueva(request):
    if request.method == "POST":

#Creamos un objeto que va a contener todos los datos que el formulario PeliculaForm nos manda a través del método POST
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():

#Guardamos primero la Película, para que exista un ID para relacionar a los actores en la tabla Actuaciones

#Como el formulario incluye campos de varias tablas, aquí es necesario indicar los campos que corresponden a Película.

            estudiante = Estudiante.objects.create(nombre=formulario.cleaned_data['nombre'], carne = formulario.cleaned_data['carne'])

#Por cada actor que esté seleccionado en el formulario, recorrerlo para guardarlo en la tabla Actuación
            for curso_id in request.POST.getlist('estudiantes'):

#A la tabla Actuación le decimos cual es el ID del Actor y el ID de Película

              estudio = Estudio(curso_id=curso_id, estudiante_id = estudiante.id)

#Vamos guardando cada actuación que va recorriendo el cilco for

              estudio.save()

#Al terminar el ciclo for, mandamos un mensaje al template para que diga que los datos se guardaron exitosamente

              messages.add_message(request, messages.SUCCESS, 'Informacion Guardada Exitosamente')
    else:
        formulario = EstudianteForm()
    return render(request, 'blog/Estudiante_editar.html', {'formulario': formulario})
