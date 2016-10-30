from django import forms

from .models import Estudiante, Curso


class EstudianteForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Estudiante
        fields = ('nombre', 'carne', 'estudiantes')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.

#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.


def __init__ (self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.

        self.fields["estudiantes"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget

        self.fields["estudiantes"].help_text = "Ingrese los Estudiantes que asignados al curso"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

        self.fields["estudiantes"].queryset = Curso.objects.all()
