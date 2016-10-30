from django.db import models
from django.contrib import admin


#Define la clase Actor, esta tabla no se relaciona con nadie más.

class Curso(models.Model):

    nombre  =   models.CharField(max_length=30)
    fecha_inscripcion = models.DateField()


    def __str__(self):

        return self.nombre


#En una misma película actúan varios actores, y un actor puede actuar en varias películas.

#Por lo tanto necesitamos una relación many to many (muchos a muchos).

#Recordemos que esto no es SQL por lo tanto las reglas de normalización como tales no se

#aplican, esto es un ORM (manejo orientado a objetos), aunque internamente la BD si sea SQL


class Estudiante(models.Model):

    nombre    = models.CharField(max_length=60)

    carne      = models.IntegerField()

 #Aquí indicamos que la propiedad actores es del tipo Many to Many.

# Y le indicamos que se relaciona con Actor a través (through) la clase Actuación, que se define más adelante.

    estudiantes   = models.ManyToManyField(Curso, through='Estudio')


    def __str__(self):

        return self.nombre


#Definimos la clase intermedia que se encargará de relacionar de uno a muchos Película y Actor.

#En esta definimos las llaves foraneas que nos relacionan a Actor y a Película.

# on_delete = models.CASCADE le indica que en caso de eliminar borre en cascada los datos relacionados.
class Estudio (models.Model):

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)


#Estas clases las usamos para indicarle a la página admin que despliegue los datos relacionados en linea.

#Es decir en el mismo formulario ambas tablas.

class EstudioInLine(admin.TabularInline):

    model = Estudio

    extra = 1


class CursoAdmin(admin.ModelAdmin):

    inlines = (EstudioInLine,)


class EstudianteAdmin (admin.ModelAdmin):

    inlines = (EstudioInLine,)
