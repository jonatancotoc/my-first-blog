#recuerde que es necesario indicar que clases de nuestro modelo van a ser manejadas por la aplicación /admin.
from django.contrib import admin
from blog.models import Estudiante, EstudianteAdmin, Curso, CursoAdmin

#Registramos nuestras clases principales.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
